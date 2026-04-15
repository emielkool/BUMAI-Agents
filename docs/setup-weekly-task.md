# Vrijdag-synthesetaak instellen in Claude.ai

Deze handleiding beschrijft hoe je de wekelijkse AI-weekoverzicht synthesetaak instelt
als tweede Claude.ai Scheduled Task. Na het instellen finaliseert Claude elke vrijdag
middag het weekoverzicht en pusht dit naar het GitHub-repo.

## Architectuur: twee taken

| Taak | Frequentie | Tijd | Doel |
|---|---|---|---|
| Dagbriefing (bestaand) | Ma–Vr | 08:00 CEST | Dagbriefing genereren + dagentry weekbestand bijwerken |
| Weekoverzicht (nieuw) | Vrijdag | 16:00 CEST | Volledige weeksyntheseanalyse finaliseren |

**Belangrijk:** de vrijdag-synthesetaak draait bewust 8 uur na de dagbriefing-taak.
Zo is de vrijdagbriefing gegarandeerd aanwezig wanneer de synthese start.

## Vereisten

- Claude.ai account (Pro, Max, Team of Enterprise)
- GitHub-repo `emielkool/bumai-agents` verbonden als connector (al ingesteld voor dagbriefing)

## Stappen

### 1. Open Scheduled Tasks

Ga naar [claude.ai](https://claude.ai) en navigeer naar **Scheduled Tasks**.

### 2. Maak een nieuwe taak aan

Klik op **New Scheduled Task**.

### 3. Verbind het GitHub-repo

Selecteer het GitHub-repo `emielkool/bumai-agents` als connected repository
(zelfde repo als de dagbriefing-taak).

### 4. Stel het schema in

- **Frequentie:** Fridays only (alleen vrijdag)
- **Tijd:** 16:00 (lokale tijd, CEST)
- **Of custom cron:** `0 14 * * 5` (14:00 UTC = 16:00 CEST zomer / 15:00 CET winter)

### 5. Plak de task prompt

Kopieer onderstaande prompt en plak deze in het promptveld van de taak:

---

```
Je bent een AI-intelligence agent voor Emiel Zuurbier (BUM AI, Ctac).

Voer de volgende stappen uit:

1. Lees het bestand `prompts/week_overzicht_prompt.md` voor de volledige
   instructies, het format en de toon van het weekoverzicht

2. Voer alle stappen uit zoals beschreven in dat bestand

Samenvatting van wat je doet:
- Bepaal het ISO weeknummer van vandaag (vrijdag)
- Lees het weekbestand voor deze week (briefings/weekoverzichten/ai-weekoverzicht-YYYY-WWW.md)
- Als Status al "Afgerond" is: stop
- Lees alle dagbriefings van deze week
- Vul de syntheseblokken in (weekhighlights, domeinpatronen, Ctac-weekperspectief, bronnenlijst)
- Zet Status op "Afgerond"
- Commit en push naar main
```

---

### 6. Activeer de taak

Sla de taak op en activeer deze. De eerste run vindt plaats op de eerstvolgende vrijdag.

## Weekbestand – locatie en naamgeving

Weekbestanden worden opgeslagen in:
```
briefings/weekoverzichten/ai-weekoverzicht-YYYY-WWW.md
```

Voorbeeld voor week 15 van 2026 (13–19 april):
```
briefings/weekoverzichten/ai-weekoverzicht-2026-W15.md
```

## Hoe werkt het samenspel?

1. **Maandag t/m vrijdag 08:00** – de dagbriefing-taak genereert de dagbriefing én
   voegt een dagentry toe aan het weekbestand (stappen 10–16 in CLAUDE.md)
2. **Vrijdag 16:00** – de synthesetaak leest alle dagentries en dagbriefings,
   schrijft de syntheseblokken, en zet `Status: Afgerond`

Het weekbestand is zo gedurende de week al leesbaar (met dagentries), en wordt
vrijdagmiddag omgezet naar een volledig strategisch weekrapport.

## Test-run

Je kunt de synthesetaak handmatig starten vanuit de Claude.ai interface om te
controleren of alles correct werkt. De taak is idempotent: als het weekbestand
al `Status: Afgerond` heeft, doet de taak niets.

## Format aanpassen

Om de synthesetekst, toon of structuur van het weekoverzicht aan te passen,
bewerk `prompts/week_overzicht_prompt.md`. Claude leest dit bestand bij elke run.
