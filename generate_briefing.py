"""
AI Dagbriefing Generator
Genereert dagelijks een AI-intelligence briefing voor Emiel Zuurbier (Ctac).

Gebruik:
    python generate_briefing.py            # vandaag
    python generate_briefing.py 2026-04-11 # specifieke datum (voor terugvullen)
"""

import sys
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path

import anthropic
import feedparser
import yaml


# ── Constanten ───────────────────────────────────────────────────────────────

CONFIG_PATH = Path("config/sources.yml")
PROMPT_PATH = Path("prompts/system_prompt.md")
BRIEFINGS_DIR = Path("briefings")
MODEL = "claude-opus-4-6"
MAX_TOKENS = 4096
MAX_SEARCHES = 12       # max web searches per run
RSS_ITEMS_PER_FEED = 5  # max items per RSS-feed
RSS_MAX_TOTAL = 25      # max RSS-items in context
RSS_AGE_HOURS = 36      # RSS-items ouder dan X uur worden weggelaten


# ── Configuratie laden ────────────────────────────────────────────────────────

def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_system_prompt() -> str:
    if PROMPT_PATH.exists():
        return PROMPT_PATH.read_text(encoding="utf-8")
    return "Je bent een AI-intelligence agent die dagelijkse briefings maakt."


# ── RSS feeds ophalen ─────────────────────────────────────────────────────────

def fetch_rss_feeds(config: dict) -> list[dict]:
    """
    Haalt recente items op uit alle geconfigureerde RSS-feeds.
    Filtert op leeftijd en sorteert op prioriteit (1 = hoogste).
    """
    cutoff = datetime.now() - timedelta(hours=RSS_AGE_HOURS)
    items = []

    for priority_key, data in config.items():
        priority_num = int(priority_key.replace("priority_", ""))
        for feed_cfg in data.get("rss_feeds", []):
            url = feed_cfg.get("url", "")
            label = feed_cfg.get("label", url)
            try:
                feed = feedparser.parse(url)
                count = 0
                for entry in feed.entries:
                    if count >= RSS_ITEMS_PER_FEED:
                        break
                    # Probeer publicatiedatum te bepalen
                    pub = None
                    if hasattr(entry, "published_parsed") and entry.published_parsed:
                        pub = datetime(*entry.published_parsed[:6])
                    if pub and pub < cutoff:
                        continue
                    items.append({
                        "priority": priority_num,
                        "label": label,
                        "title": entry.get("title", "").strip(),
                        "link": entry.get("link", ""),
                        "summary": entry.get("summary", "")[:300].strip(),
                    })
                    count += 1
            except Exception as exc:
                print(f"  ⚠️  RSS fout ({label}): {exc}")

    # Sorteer: eerst hoge prioriteit, dan recenter
    items.sort(key=lambda x: x["priority"])
    return items[:RSS_MAX_TOTAL]


# ── Prompt opbouwen ───────────────────────────────────────────────────────────

def build_source_instructions(config: dict) -> str:
    """Vertaalt sources.yml naar leesbare zoekinstructies voor Claude."""
    lines = []
    labels = {1: "**altijd**", 2: "**bij voorkeur**", 3: "aanvullend"}
    for priority_key, data in config.items():
        num = int(priority_key.replace("priority_", ""))
        sites = data.get("sites", [])
        if not sites:
            continue
        formatted = ", ".join(
            f"`{s['domain']}` ({s.get('label', '')})" for s in sites
        )
        lines.append(f"- Prioriteit {num} ({labels.get(num, '')}): {formatted}")
    return "\n".join(lines)


def build_rss_context(items: list[dict]) -> str:
    """Formatteert RSS-items als context voor Claude."""
    if not items:
        return ""
    lines = ["## Recente headlines uit geconfigureerde feeds\n"]
    for item in items:
        lines.append(f"- **[P{item['priority']}] {item['label']}**: "
                     f"[{item['title']}]({item['link']})")
        if item["summary"]:
            lines.append(f"  > {item['summary'][:150]}…")
    return "\n".join(lines)


def build_user_message(target_date: date, config: dict, rss_items: list[dict]) -> str:
    date_nl = target_date.strftime("%-d %B %Y")
    source_instructions = build_source_instructions(config)
    rss_context = build_rss_context(rss_items)

    return f"""Genereer de AI dagbriefing voor {date_nl}.

## Zoekinstructies

Gebruik de `web_search` tool om actueel nieuws op te zoeken. Houd de volgende prioriteiten aan:

{source_instructions}

Voer minimaal 6 gerichte zoekopdrachten uit, verspreid over de domeinen:
Technologie & Modellen, Governance & Beleid, Security & Risk, Markt & Adoptie.

{rss_context}

Schrijf daarna de volledige briefing in het voorgeschreven Markdown-format.
Sluit elke sectie af met de gebruikte bronnen (URLs).
"""


# ── Claude aanroepen ──────────────────────────────────────────────────────────

def call_claude(system_prompt: str, user_message: str) -> str:
    """
    Roept Claude aan met de web_search tool.
    Herstart automatisch bij pause_turn (server-side loop limiet).
    """
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": user_message}]
    tools = [{
        "type": "web_search_20260209",
        "name": "web_search",
        "max_uses": MAX_SEARCHES,
    }]

    max_continuations = 3
    for attempt in range(max_continuations):
        print(f"  → API-aanroep {attempt + 1}/{max_continuations}…")
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )

        if response.stop_reason == "pause_turn":
            # Server-side loop limiet bereikt; ga verder
            print("  ℹ️  pause_turn ontvangen – doorgaan…")
            messages.append({"role": "assistant", "content": response.content})
            continue

        # end_turn of iets anders → klaar
        break

    # Extraheer de gegenereerde tekst
    text_parts = [
        block.text
        for block in response.content
        if hasattr(block, "type") and block.type == "text"
    ]
    return "\n\n".join(text_parts).strip()


# ── Opslaan & committen ───────────────────────────────────────────────────────

def save_briefing(briefing: str, target_date: date) -> Path:
    date_str = target_date.strftime("%Y-%m-%d")
    output_path = BRIEFINGS_DIR / f"ai-briefing-{date_str}.md"
    BRIEFINGS_DIR.mkdir(exist_ok=True)
    output_path.write_text(briefing, encoding="utf-8")
    print(f"  ✅ Opgeslagen: {output_path}")
    return output_path


def git_commit_and_push(output_path: Path, target_date: date) -> None:
    date_str = target_date.strftime("%Y-%m-%d")
    cmds = [
        ["git", "config", "user.email", "ai-agent@ctac.nl"],
        ["git", "config", "user.name", "AI Briefing Agent"],
        ["git", "add", str(output_path)],
        ["git", "commit", "-m", f"briefing: dagelijkse AI-briefing {date_str}"],
        ["git", "push"],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ⚠️  Git commando mislukt: {' '.join(cmd)}")
            print(f"     {result.stderr.strip()}")
            raise RuntimeError(f"Git fout: {result.stderr.strip()}")
    print("  ✅ Gepusht naar GitHub")


# ── Hoofdfunctie ──────────────────────────────────────────────────────────────

def main() -> None:
    # Optioneel: datum als argument meegeven (format: YYYY-MM-DD)
    if len(sys.argv) > 1:
        try:
            target_date = date.fromisoformat(sys.argv[1])
        except ValueError:
            print(f"Ongeldige datum: {sys.argv[1]}. Gebruik YYYY-MM-DD.")
            sys.exit(1)
    else:
        target_date = date.today()

    print(f"\n🗞️  AI Dagbriefing Generator – {target_date}")
    print("=" * 50)

    # Controleer of briefing al bestaat
    date_str = target_date.strftime("%Y-%m-%d")
    output_path = BRIEFINGS_DIR / f"ai-briefing-{date_str}.md"
    if output_path.exists():
        print(f"  ℹ️  Briefing bestaat al: {output_path}")
        print("  Verwijder het bestand handmatig om opnieuw te genereren.")
        sys.exit(0)

    print("\n1. Configuratie laden…")
    config = load_config()
    system_prompt = load_system_prompt()

    print("2. RSS feeds ophalen…")
    rss_items = fetch_rss_feeds(config)
    print(f"   {len(rss_items)} recente items gevonden")

    user_message = build_user_message(target_date, config, rss_items)

    print("3. Claude aanroepen (web search ingeschakeld)…")
    briefing = call_claude(system_prompt, user_message)

    if not briefing:
        print("  ❌ Geen tekst gegenereerd. Controleer de API-aanroep.")
        sys.exit(1)

    print("4. Briefing opslaan…")
    output_path = save_briefing(briefing, target_date)

    print("5. Committen en pushen…")
    try:
        git_commit_and_push(output_path, target_date)
    except RuntimeError:
        print("  ⚠️  Push mislukt – briefing is wél lokaal opgeslagen.")
        sys.exit(1)

    print(f"\n✅ Klaar! Briefing beschikbaar: {output_path}\n")


if __name__ == "__main__":
    main()
