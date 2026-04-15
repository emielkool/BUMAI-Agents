# AI Dagbriefing – Repository-instructies

Dit repo bevat configuratie en output voor de dagelijkse AI-intelligence briefing
voor Emiel Zuurbier (BUM AI, Ctac).

## Structuur

- `config/sources.yml` – Bronnenconfiguratie met 3 prioriteitsniveaus
- `prompts/system_prompt.md` – Volledige briefing-instructies, format en tone-of-voice
- `prompts/week_overzicht_prompt.md` – Instructies voor de vrijdag-synthesetaak
- `briefings/` – Gegenereerde dagbriefings (één per werkdag)
- `briefings/weekoverzichten/` – Weekoverzichten per ISO-weeknummer
- `docs/setup-scheduled-task.md` – Handleiding voor de dagelijkse Scheduled Task
- `docs/setup-weekly-task.md` – Handleiding voor de vrijdag-synthesetaak

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

## Bij het updaten van het weekoverzicht

Voer stappen 10–16 uit **na** stap 9 (push van de dagbriefing).

10. Bepaal het ISO weeknummer van vandaag
    - Gebruik ISO 8601: de week die de eerste donderdag van het jaar bevat is week 1
    - Formaat weekbestand: `briefings/weekoverzichten/ai-weekoverzicht-YYYY-WWW.md`
    - Voorbeeld: maandag 13 april 2026 = Week 15 → `ai-weekoverzicht-2026-W15.md`
    - Bepaal ook de weekperiode: maandag t/m zondag van die week

11. Controleer of de dagentry van vandaag al aanwezig is in het weekbestand
    - Zoek naar de koptekst `### [Dagnaam] [dag maand]` (bijv. `### Woensdag 15 april`)
    - Als de entry al bestaat: sla stappen 13–16 over (idempotentiecheck)

12. Controleer of het weekbestand al bestaat
    - **Zo niet:** maak het aan met de volledige structuur:
      - YAML frontmatter (zie format hieronder)
      - Dagkopteksten voor alle 5 werkdagen (maandag t/m vrijdag)
      - Eerdere dagen die ontbreken krijgen: `*(geen briefing beschikbaar voor deze dag)*`
      - Lege syntheseblokken met placeholdertekst (zie format)
    - **Zo wel:** lees het bestaande bestand, voeg alleen de dagentry van vandaag toe

    **YAML frontmatter weekbestand:**
    ```
    ---
    Stakeholders:
      - Emiel Kool
      - Eloy Schultz
    Week: YYYY-WWW
    Periode: YYYY-MM-DD / YYYY-MM-DD
    Status: In uitvoering
    tags:
      - weekoverzicht
    ---
    ```

13. Schrijf de dagentry van vandaag in het weekbestand:
    - Koptekst: `### [Dagnaam] [dag maand]` (bijv. `### Woensdag 15 april`)
    - Link naar dagbriefing: `→ Dagbriefing: [ai-briefing-YYYY-MM-DD.md](../ai-briefing-YYYY-MM-DD.md)`
    - **Highlights:** 3 bullets uit de dagbriefing (maximaal 2 zinnen elk)
    - **Ctac-relevantie van de dag:** 1–2 zinnen strategische kern uit de dagbriefing
    - Sluit de dagentry af met een horizontale regel `---`

14. (Idempotentiecheck — zie stap 11: als entry al bestond, stop hier)

15. Commit het weekbestand:
    - Bericht: `weekoverzicht: dagentry YYYY-MM-DD toegevoegd aan week YYYY-WWW`
    - Voorbeeld: `weekoverzicht: dagentry 2026-04-15 toegevoegd aan week 2026-W15`

16. Push naar main: `git push origin HEAD:main`
