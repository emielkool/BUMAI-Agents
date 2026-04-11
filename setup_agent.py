"""
AI Briefing Agent – Eenmalige setup
====================================
Maak de Anthropic Managed Agent en omgeving aan.
Voer dit eenmalig uit en sla de geprinte IDs op als GitHub Secrets.

Gebruik:
    python setup_agent.py            # nieuw aanmaken
    python setup_agent.py --update   # bestaande agent updaten (systeemprompt)

Vereist:
    ANTHROPIC_API_KEY als omgevingsvariabele
    pip install -r requirements.txt
"""

import os
import sys
from pathlib import Path

import anthropic

PROMPT_PATH = Path("prompts/system_prompt.md")
AGENT_NAME = "AI Dagbriefing Agent – Ctac"
ENV_NAME = "briefing-environment"


def load_system_prompt() -> str:
    if not PROMPT_PATH.exists():
        print(f"❌ Systeemprompt niet gevonden: {PROMPT_PATH}")
        sys.exit(1)
    return PROMPT_PATH.read_text(encoding="utf-8")


def create_environment(client: anthropic.Anthropic) -> str:
    """Maakt de cloud-omgeving aan. Web search vereist unrestricted netwerk."""
    print("1. Omgeving aanmaken…")
    env = client.beta.environments.create(
        name=ENV_NAME,
        config={
            "type": "cloud",
            "networking": {"type": "unrestricted"},  # web search vereist internet
        },
    )
    print(f"   ✅ Omgeving aangemaakt: {env.id}")
    return env.id


def create_agent(client: anthropic.Anthropic, system_prompt: str) -> tuple[str, str]:
    """Maakt de agent aan. Geeft (agent_id, agent_version) terug."""
    print("2. Agent aanmaken…")
    agent = client.beta.agents.create(
        name=AGENT_NAME,
        model="claude-opus-4-6",
        description="Dagelijkse AI-intelligence briefing voor Emiel Zuurbier (BUM AI, Ctac).",
        system=system_prompt,
        tools=[{
            "type": "agent_toolset_20260401",
            "default_config": {"enabled": True},
            # agent_toolset bevat: bash, read, write, edit, glob, grep,
            # web_fetch én web_search – alles wat de agent nodig heeft
        }],
    )
    print(f"   ✅ Agent aangemaakt : {agent.id}")
    print(f"   ✅ Versie           : {agent.version}")
    return agent.id, str(agent.version)


def update_agent(client: anthropic.Anthropic, agent_id: str, system_prompt: str) -> str:
    """Update de systeemprompt van een bestaande agent (maakt nieuwe versie)."""
    print(f"2. Agent updaten ({agent_id})…")
    agent = client.beta.agents.update(
        agent_id,
        system=system_prompt,
    )
    print(f"   ✅ Nieuwe versie: {agent.version}")
    return str(agent.version)


def print_next_steps(agent_id: str, agent_version: str, env_id: str) -> None:
    print("\n" + "=" * 60)
    print("✅  Setup klaar! Voeg deze secrets toe aan GitHub:")
    print("    Repo → Settings → Secrets and variables → Actions")
    print("=" * 60)
    print(f"\n  ANTHROPIC_API_KEY  = <jouw key van console.anthropic.com>")
    print(f"  AGENT_ID           = {agent_id}")
    print(f"  AGENT_VERSION      = {agent_version}  (optioneel – voor pinning)")
    print(f"  ENV_ID             = {env_id}")
    print("\nNa het toevoegen van de secrets kun je de GitHub Action")
    print("handmatig starten via: Actions → Dagelijkse AI Briefing → Run workflow\n")


def main() -> None:
    update_mode = "--update" in sys.argv

    client = anthropic.Anthropic()
    system_prompt = load_system_prompt()

    if update_mode:
        agent_id = os.environ.get("AGENT_ID")
        env_id = os.environ.get("ENV_ID")
        if not agent_id or not env_id:
            print("❌ Zet AGENT_ID en ENV_ID als omgevingsvariabele voor --update.")
            sys.exit(1)
        agent_version = update_agent(client, agent_id, system_prompt)
        print(f"\n✅  Agent bijgewerkt. Nieuwe AGENT_VERSION: {agent_version}")
        print("    Update de GitHub Secret indien je op een vaste versie pinned.")
    else:
        env_id = create_environment(client)
        agent_id, agent_version = create_agent(client, system_prompt)
        print_next_steps(agent_id, agent_version, env_id)


if __name__ == "__main__":
    main()
