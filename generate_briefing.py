"""
AI Dagbriefing Generator – Managed Agents versie
=================================================
Gebruikt een Anthropic Managed Agent (persistent, versioned) om
dagelijks een AI-intelligence briefing te genereren.

Voer eerst setup_agent.py uit om de agent + omgeving aan te maken.
Daarna sla je AGENT_ID en ENV_ID op als GitHub Secrets.

Gebruik:
    python generate_briefing.py            # vandaag
    python generate_briefing.py 2026-04-11 # specifieke datum (terugvullen)

Vereiste omgevingsvariabelen:
    ANTHROPIC_API_KEY
    AGENT_ID          (uit setup_agent.py)
    ENV_ID            (uit setup_agent.py)
"""

import os
import sys
import time
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path

import anthropic
import feedparser
import yaml


# ── Constanten ───────────────────────────────────────────────────────────────

CONFIG_PATH   = Path("config/sources.yml")
BRIEFINGS_DIR = Path("briefings")
RSS_ITEMS_PER_FEED = 5   # max items per RSS-feed
RSS_MAX_TOTAL      = 25  # max RSS-items in context
RSS_AGE_HOURS      = 36  # items ouder dan X uur worden weggelaten


# ── Configuratie laden ────────────────────────────────────────────────────────

def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"❌  Omgevingsvariabele ontbreekt: {name}")
        print("    Voer setup_agent.py uit en stel de secrets in.")
        sys.exit(1)
    return value


# ── RSS feeds ophalen ─────────────────────────────────────────────────────────

def fetch_rss_feeds(config: dict) -> list[dict]:
    """Haalt recente items op uit alle geconfigureerde RSS-feeds."""
    cutoff = datetime.now() - timedelta(hours=RSS_AGE_HOURS)
    items = []

    for priority_key, data in config.items():
        priority_num = int(priority_key.replace("priority_", ""))
        for feed_cfg in data.get("rss_feeds", []):
            url   = feed_cfg.get("url", "")
            label = feed_cfg.get("label", url)
            try:
                feed  = feedparser.parse(url)
                count = 0
                for entry in feed.entries:
                    if count >= RSS_ITEMS_PER_FEED:
                        break
                    pub = None
                    if hasattr(entry, "published_parsed") and entry.published_parsed:
                        pub = datetime(*entry.published_parsed[:6])
                    if pub and pub < cutoff:
                        continue
                    items.append({
                        "priority": priority_num,
                        "label":    label,
                        "title":    entry.get("title", "").strip(),
                        "link":     entry.get("link", ""),
                        "summary":  entry.get("summary", "")[:300].strip(),
                    })
                    count += 1
            except Exception as exc:
                print(f"  ⚠️  RSS fout ({label}): {exc}")

    items.sort(key=lambda x: x["priority"])
    return items[:RSS_MAX_TOTAL]


# ── Bericht opbouwen ──────────────────────────────────────────────────────────

def build_source_instructions(config: dict) -> str:
    labels = {1: "**altijd**", 2: "**bij voorkeur**", 3: "aanvullend"}
    lines  = []
    for priority_key, data in config.items():
        num   = int(priority_key.replace("priority_", ""))
        sites = data.get("sites", [])
        if not sites:
            continue
        formatted = ", ".join(
            f"`{s['domain']}` ({s.get('label', '')})" for s in sites
        )
        lines.append(f"- Prioriteit {num} ({labels.get(num, '')}): {formatted}")
    return "\n".join(lines)


def build_rss_context(items: list[dict]) -> str:
    if not items:
        return ""
    lines = ["## Recente headlines uit geconfigureerde feeds\n"]
    for item in items:
        lines.append(
            f"- **[P{item['priority']}] {item['label']}**: "
            f"[{item['title']}]({item['link']})"
        )
        if item["summary"]:
            lines.append(f"  > {item['summary'][:150]}…")
    return "\n".join(lines)


def build_user_message(target_date: date, config: dict, rss_items: list[dict]) -> str:
    date_nl            = target_date.strftime("%-d %B %Y")
    source_instructions = build_source_instructions(config)
    rss_context        = build_rss_context(rss_items)

    return f"""Genereer de AI dagbriefing voor {date_nl}.

## Zoekinstructies

Gebruik de `web_search` tool om actueel nieuws op te zoeken.
Houd de volgende prioriteiten aan bij het kiezen van bronnen:

{source_instructions}

Voer minimaal 6 gerichte zoekopdrachten uit, verspreid over de domeinen:
Technologie & Modellen, Governance & Beleid, Security & Risk, Markt & Adoptie.

{rss_context}

Schrijf daarna de volledige briefing in het voorgeschreven Markdown-format.
Vermeld bij elke bevinding de bron (URL).
"""


# ── Managed Agent sessie uitvoeren ────────────────────────────────────────────

def run_agent_session(
    client:       anthropic.Anthropic,
    agent_id:     str,
    env_id:       str,
    user_message: str,
) -> str:
    """
    Maakt een sessie aan, stuurt het bericht, streamt de events en
    geeft de gegenereerde briefing-tekst terug.
    """

    # 1. Sessie aanmaken
    print("  → Sessie aanmaken…")
    session = client.beta.sessions.create(
        agent=agent_id,       # gebruikt altijd de laatste versie
        environment_id=env_id,
    )
    print(f"  → Sessie: {session.id}")

    briefing_parts: list[str] = []

    try:
        # 2. Stream openen vóór het sturen van het bericht (stream-first patroon)
        with client.beta.sessions.stream(session_id=session.id) as stream:

            # 3. Bericht insturen terwijl de stream open is
            client.beta.sessions.events.send(
                session_id=session.id,
                events=[{
                    "type":    "user.message",
                    "content": [{"type": "text", "text": user_message}],
                }],
            )

            # 4. Events verwerken
            for event in stream:
                if event.type == "agent.message":
                    # Verzamel alle tekst-blokken van de agent
                    for block in event.content:
                        if hasattr(block, "type") and block.type == "text":
                            briefing_parts.append(block.text)

                elif event.type == "agent.tool_use":
                    tool = getattr(event, "name", "?")
                    print(f"  🔍 Tool: {tool}")

                elif event.type == "session.status_idle":
                    # Controleer of er een actie vereist is (zou niet mogen
                    # voorkomen zonder custom tools)
                    stop_type = getattr(
                        getattr(event, "stop_reason", None), "type", "end_turn"
                    )
                    if stop_type != "requires_action":
                        break   # normaal klaar

                elif event.type == "session.status_terminated":
                    print("  ⚠️  Sessie onverwacht beëindigd.")
                    break

    finally:
        # 5. Sessie opschonen – wacht kort op de status-write race
        time.sleep(1)
        try:
            client.beta.sessions.delete(session_id=session.id)
            print(f"  → Sessie verwijderd: {session.id}")
        except Exception as exc:
            print(f"  ⚠️  Sessie verwijderen mislukt (niet kritiek): {exc}")

    return "\n\n".join(briefing_parts).strip()


# ── Opslaan & committen ───────────────────────────────────────────────────────

def save_briefing(briefing: str, target_date: date) -> Path:
    date_str     = target_date.strftime("%Y-%m-%d")
    output_path  = BRIEFINGS_DIR / f"ai-briefing-{date_str}.md"
    BRIEFINGS_DIR.mkdir(exist_ok=True)
    output_path.write_text(briefing, encoding="utf-8")
    print(f"  ✅ Opgeslagen: {output_path}")
    return output_path


def git_commit_and_push(output_path: Path, target_date: date) -> None:
    date_str = target_date.strftime("%Y-%m-%d")
    cmds = [
        ["git", "config", "user.email", "ai-agent@ctac.nl"],
        ["git", "config", "user.name",  "AI Briefing Agent"],
        ["git", "add",    str(output_path)],
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
    # Optioneel: datum als CLI-argument (YYYY-MM-DD)
    if len(sys.argv) > 1:
        try:
            target_date = date.fromisoformat(sys.argv[1])
        except ValueError:
            print(f"Ongeldige datum: {sys.argv[1]}. Gebruik YYYY-MM-DD.")
            sys.exit(1)
    else:
        target_date = date.today()

    print(f"\n🗞️  AI Dagbriefing – {target_date}  (Managed Agent)")
    print("=" * 55)

    # Controleer of briefing al bestaat
    date_str    = target_date.strftime("%Y-%m-%d")
    output_path = BRIEFINGS_DIR / f"ai-briefing-{date_str}.md"
    if output_path.exists():
        print(f"  ℹ️  Briefing bestaat al: {output_path}")
        print("  Verwijder het bestand handmatig om opnieuw te genereren.")
        sys.exit(0)

    # Vereiste omgevingsvariabelen
    agent_id = get_required_env("AGENT_ID")
    env_id   = get_required_env("ENV_ID")
    client   = anthropic.Anthropic()

    print("\n1. Configuratie laden…")
    config = load_config()

    print("2. RSS feeds ophalen…")
    rss_items = fetch_rss_feeds(config)
    print(f"   {len(rss_items)} recente items gevonden")

    user_message = build_user_message(target_date, config, rss_items)

    print("3. Agent-sessie starten…")
    briefing = run_agent_session(client, agent_id, env_id, user_message)

    if not briefing:
        print("  ❌ Geen tekst ontvangen van de agent.")
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
