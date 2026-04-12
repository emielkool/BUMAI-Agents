# AI Dagbriefing – Repository-instructies

Dit repo bevat configuratie en output voor de dagelijkse AI-intelligence briefing
voor Emiel Zuurbier (BUM AI, Ctac).

## Structuur

- `config/sources.yml` – Bronnenconfiguratie met 3 prioriteitsniveaus
- `prompts/system_prompt.md` – Volledige briefing-instructies, format en tone-of-voice
- `briefings/` – Gegenereerde briefings (één per werkdag)
- `docs/setup-scheduled-task.md` – Handleiding voor het instellen van de Scheduled Task

## Bij het genereren van een briefing

1. Lees `prompts/system_prompt.md` voor de volledige instructies, tone-of-voice en Markdown-structuur
2. Lees `config/sources.yml` voor de bronnenprioritering
3. Bepaal de datum van vandaag
4. Controleer of `briefings/ai-briefing-{datum}.md` al bestaat — zo ja, stop
5. Gebruik web search om actueel AI-nieuws op te halen (minimaal 6 zoekopdrachten)
   - Verdeel over de domeinen: Technologie & Modellen, Governance & Beleid, Security & Risk, Markt & Adoptie
   - Prioriteer bronnen uit `sources.yml` (prioriteit 1 = altijd, 2 = bij voorkeur, 3 = aanvullend)
6. Genereer de briefing volgens het voorgeschreven format
7. Sla op als `briefings/ai-briefing-YYYY-MM-DD.md`
8. Commit met bericht: `briefing: dagelijkse AI-briefing YYYY-MM-DD`
9. Push direct naar de main branch: `git push origin HEAD:main`
   (Dit zorgt dat de briefing op main terechtkomt, ongeacht de huidige branch)
