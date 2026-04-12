# Scheduled Task instellen in Claude.ai

Deze handleiding beschrijft hoe je de dagelijkse AI-briefing instelt als
Claude.ai Scheduled Task. Na het instellen genereert Claude elke werkdag
automatisch een briefing en pusht deze naar het GitHub-repo.

## Vereisten

- Claude.ai account (Pro, Max, Team of Enterprise)
- GitHub-repo `emielkool/bumai-agents` verbonden als connector

## Stappen

### 1. Open Scheduled Tasks

Ga naar [claude.ai](https://claude.ai) en navigeer naar **Scheduled Tasks**
(via het menu of de instellingen).

### 2. Maak een nieuwe taak aan

Klik op **New Scheduled Task** (of vergelijkbaar).

### 3. Verbind het GitHub-repo

Selecteer het GitHub-repo `emielkool/bumai-agents` als connected repository.
Als het repo nog niet verbonden is, volg de stappen om de GitHub-connector
te activeren.

### 4. Stel het schema in

- **Frequentie:** Weekdays (maandag t/m vrijdag)
- **Tijd:** 08:00 (lokale tijd, CEST)
- **Of custom cron:** `0 6 * * 1-5` (06:00 UTC = 08:00 CEST zomer / 07:00 CET winter)

### 5. Plak de task prompt

Kopieer onderstaande prompt en plak deze in het promptveld van de taak:

---

```
Je bent een AI-intelligence agent voor Emiel Zuurbier (BUM AI, Ctac).
Voer de volgende stappen uit:

1. Lees het bestand `prompts/system_prompt.md` voor je rol, tone-of-voice
   en het exacte Markdown-format van de briefing
2. Lees `config/sources.yml` voor de bronnenprioritering
3. Bepaal de datum van vandaag (formaat: YYYY-MM-DD)
4. Controleer of `briefings/ai-briefing-{datum}.md` al bestaat — zo ja, stop
5. Zoek met web search naar actueel AI-nieuws van vandaag en gisteren:
   - Voer minimaal 6 gerichte zoekopdrachten uit
   - Verdeel over de domeinen: Technologie & Modellen, Governance & Beleid,
     Security & Risk, Markt & Adoptie
   - Prioriteer bronnen uit sources.yml:
     prioriteit 1 = altijd doorzoeken,
     prioriteit 2 = bij voorkeur,
     prioriteit 3 = aanvullend
6. Schrijf de briefing volgens het format uit system_prompt.md
   - Maximaal ~600-800 woorden
   - In het Nederlands
   - Vermeld bij elke bevinding de bron (URL)
   - Wees kritisch: niet elke aankondiging is een doorbraak
7. Sla op als `briefings/ai-briefing-{datum}.md`
8. Commit met bericht: `briefing: dagelijkse AI-briefing {datum}`
9. Push direct naar de main branch: `git push origin HEAD:main`
   (Dit zorgt dat de briefing op main terechtkomt, ongeacht de huidige werkomgeving)
```

---

### 6. Activeer de taak

Sla de taak op en activeer deze. De eerste run vindt plaats op de
eerstvolgende werkdag volgens het ingestelde schema.

## Test-run

Je kunt de taak handmatig starten vanuit de Claude.ai interface om te
controleren of alles correct werkt voordat je wacht op de automatische run.

## Bronnen aanpassen

Om bronnen toe te voegen of prioriteiten te wijzigen, bewerk
`config/sources.yml` in het repo. Claude leest dit bestand bij elke run.

## Briefing-format aanpassen

Om het format, de tone-of-voice of de domeinen aan te passen, bewerk
`prompts/system_prompt.md`. Claude leest dit bestand bij elke run.
