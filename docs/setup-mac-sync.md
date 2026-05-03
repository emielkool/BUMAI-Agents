# Mac-synchronisatie instellen

De dagelijkse briefings en weekoverzichten worden door de Claude.ai Scheduled Task naar GitHub gepusht.
Een macOS LaunchAgent haalt ze elke ochtend automatisch op en kopieert ze naar de juiste mappen in je Obsidian vault.

## Hoe het werkt

- Scheduler pusht om **07:00** naar GitHub
- LaunchAgent draait om **07:30** op je Mac:
  1. `git fetch + checkout + reset` — repo identiek aan remote main
  2. Nieuwste `ai-briefing-*.md` → OneDrive map **AI Briefings/briefings/**
  3. Nieuwste `ai-weekoverzicht-*.md` → OneDrive map **AI Briefings/briefings/weekoverzichten/**

---

## Installatie (éénmalig, ~5 minuten)

### Stap 1 – Verwijder eventuele oude LaunchAgents

Als je eerder een versie had geïnstalleerd, verwijder die eerst:

```bash
launchctl bootout gui/$(id -u)/com.ctac.bumai-sync 2>/dev/null
launchctl bootout gui/$(id -u)/com.ctac.bumai-weekoverzicht-sync 2>/dev/null
rm -f ~/Library/LaunchAgents/com.ctac.bumai*.plist
```

### Stap 2 – Zoek je repo-pad op

```bash
find ~ -type d -name "BUMAI-Agents" -maxdepth 6 2>/dev/null
```

Of open **GitHub Desktop** → rechtsklik op het repo → **Show in Finder**.

### Stap 3 – Zorg dat git auth geconfigureerd is

```bash
cd /pad/naar/repo
git fetch origin main && git checkout main && git reset --hard origin/main
```

Als dit zonder wachtwoordprompt werkt, is de authenticatie goed.

### Stap 4 – Installeer de LaunchAgent

Kopieer onderstaand blok, pas de drie variabelen aan, en plak het in Terminal:

```bash
REPO_PATH="/pad/naar/BUMAI-Agents"
ONEDRIVE_DAG="/Users/emiel.kool/Library/CloudStorage/OneDrive-Gedeeldebibliotheken-Ctac/AI Unit - Documents/General/AI BU Notitie Vault/3. Organisatorisch/AI Briefings/briefings"
ONEDRIVE_WEEK="/Users/emiel.kool/Library/CloudStorage/OneDrive-Gedeeldebibliotheken-Ctac/AI Unit - Documents/General/AI BU Notitie Vault/3. Organisatorisch/AI Briefings/briefings/weekoverzichten"

sed \
  -e "s|REPO_PATH_PLACEHOLDER|$REPO_PATH|g" \
  -e "s|ONEDRIVE_DAGBRIEFINGS_PLACEHOLDER|$ONEDRIVE_DAG|g" \
  -e "s|ONEDRIVE_WEEKOVERZICHTEN_PLACEHOLDER|$ONEDRIVE_WEEK|g" \
  "$REPO_PATH/scripts/com.ctac.bumai-sync.plist" \
  > ~/Library/LaunchAgents/com.ctac.bumai-sync.plist

launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ctac.bumai-sync.plist
```

### Stap 5 – Controleer of het werkt

```bash
launchctl list | grep bumai
```

Je ziet `com.ctac.bumai-sync` als de agent actief is.

---

## Handmatig een sync triggeren

```bash
launchctl kickstart gui/$(id -u)/com.ctac.bumai-sync
```

Log inzien:

```bash
cat /tmp/bumai-sync.log
```

---

## Verwijderen

```bash
launchctl bootout gui/$(id -u)/com.ctac.bumai-sync
rm ~/Library/LaunchAgents/com.ctac.bumai-sync.plist
```

---

## Geïnstalleerde bestanden

| Locatie | Doel |
|---------|------|
| `~/Library/LaunchAgents/com.ctac.bumai-sync.plist` | LaunchAgent (met ingevulde paden) |
| `scripts/bumai-sync.sh` in de repo | Bash-script dat git sync en kopieën uitvoert |
