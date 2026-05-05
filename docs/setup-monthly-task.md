# Maandelijkse Scheduled Task instellen in Claude.ai

Deze handleiding beschrijft hoe je de maandelijkse AI-maandoverzicht instelt als
Claude.ai Scheduled Task. De taak draait automatisch op de 1e van elke maand en
synthetiseert alle weekoverzichten van de vorige maand.

## Vereisten

- Claude.ai account (Pro, Max, Team of Enterprise)
- GitHub-repo `emielkool/bumai-agents` verbonden als connector
- Weekoverzichten worden al gegenereerd door de wekelijkse taak

## Stappen

### 1. Open Scheduled Tasks

Ga naar [claude.ai](https://claude.ai) en navigeer naar **Scheduled Tasks**.

### 2. Maak een nieuwe taak aan

Klik op **New Scheduled Task**.

### 3. Verbind het GitHub-repo

Selecteer het GitHub-repo `emielkool/bumai-agents` als connected repository.

### 4. Stel het schema in

- **Frequentie:** Monthly, op de 1e van de maand
- **Tijd:** 08:00 (lokale tijd, CEST)
- **Of custom cron:** `0 6 1 * *` (06:00 UTC = 08:00 CEST zomer / 07:00 CET winter)

### 5. Plak de task prompt

Kopieer onderstaande prompt en plak deze in het promptveld van de taak:

---

```
Je bent een AI-intelligence agent voor Emiel Zuurbier (BUM AI, Ctac).
Voer de volgende stappen uit:

1. Lees het bestand `prompts/maand_overzicht_prompt.md` voor je rol, tone-of-voice
   en het exacte Markdown-format van het maandoverzicht
2. Bepaal de vorige maand (formaat: YYYY-MM)
   - Vandaag is de 1e van de huidige maand → vorige maand is het onderwerp
   - Voorbeeld: op 1 mei 2026 → vorige maand = 2026-04 (april 2026)
3. Controleer of `briefings/maandoverzichten/ai-maandoverzicht-{YYYY-MM}.md` al
   bestaat en Status: Afgerond heeft — zo ja, stop
4. Lees alle weekoverzichten in `briefings/weekoverzichten/` waarvan de Periode
   (deels) in de vorige maand valt
5. Schrijf het maandoverzicht volgens het format uit maand_overzicht_prompt.md
   - Synthese op maandniveau, niet een opsomming van weken
   - Identificeer dominante thema's en verschuivingen over de maand heen
6. Sla op als `briefings/maandoverzichten/ai-maandoverzicht-{YYYY-MM}.md`
7. Commit met bericht: `maandoverzicht: AI maandoverzicht {YYYY-MM}`
8. Push direct naar de main branch: `git push origin HEAD:main`
```

---

### 6. Activeer de taak

Sla de taak op en activeer deze. De eerste run vindt plaats op de 1e van de
eerstvolgende maand.

## Test-run

Je kunt de taak handmatig starten vanuit de Claude.ai interface. Zorg dat er
weekoverzichten beschikbaar zijn voor de vorige maand voordat je test.

## Relatie tot andere taken

| Taak | Frequentie | Output |
|------|-----------|--------|
| Dagbriefing | Werkdagen 08:00 | `briefings/dagoverzichten/` |
| Weekoverzicht | Vrijdag 08:00 | `briefings/weekoverzichten/` |
| Maandoverzicht | 1e van de maand 08:00 | `briefings/maandoverzichten/` |

Het maandoverzicht bouwt voort op de weekoverzichten — zorg dat de wekelijkse
taak correct draait voordat je het maandoverzicht configureert.
