# Mac-synchronisatie instellen

De dagelijkse briefings worden door de Claude.ai Scheduled Task naar GitHub gepusht.
Zet een macOS LaunchAgent in om ze elke ochtend automatisch naar je Mac te halen —
30 minuten nadat de scheduler heeft gedraaid.

## Hoe het werkt

- Scheduler pusht om **08:00** naar GitHub
- LaunchAgent doet een `git pull` om **08:30** op je Mac, elke dag
- De nieuwe briefing staat dan klaar in je lokale repo

---

## Installatie (éénmalig, ~3 minuten)

### Stap 1 – Zoek je repo-pad op

Open Terminal en voer uit:

```bash
find ~ -type d -name "BUMAI-Agents" -maxdepth 6 2>/dev/null
```

Of open **GitHub Desktop** → rechtsklik op het repo → **Show in Finder**.

### Stap 2 – Zorg dat git auth geconfigureerd is

```bash
cd /pad/naar/repo
git pull origin main
```

Als dit zonder wachtwoordprompt werkt, is de authenticatie goed ingesteld.

### Stap 3 – Installeer de LaunchAgent

Kopieer onderstaand commando en vervang `/PAD/NAAR/BUMAI-AGENTS` met je eigen repo-pad:

```bash
REPO_PATH="/PAD/NAAR/BUMAI-AGENTS"

sed "s|REPO_PATH_PLACEHOLDER|$REPO_PATH|g" \
  "$REPO_PATH/scripts/com.ctac.bumai-sync.plist" \
  > ~/Library/LaunchAgents/com.ctac.bumai-sync.plist

launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ctac.bumai-sync.plist
```

### Stap 4 – Controleer of het werkt

```bash
launchctl list | grep bumai
```

Je ziet `com.ctac.bumai-sync` als de agent actief is.

---

## Handmatig een sync triggeren

```bash
launchctl kickstart gui/$(id -u)/com.ctac.bumai-sync
```

Logs inzien:

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

## Gebruik je Obsidian?

Als je de briefings in Obsidian leest, zorg dan dat je vault naar de `briefings/`-map
van de repo wijst (of de repo als vault gebruikt). De LaunchAgent pullt de nieuwe
bestanden automatisch, zodat ze bij het openen van Obsidian al aanwezig zijn.

Optioneel: installeer de **Obsidian Git**-plugin voor extra sync-mogelijkheden vanuit
de Obsidian UI zelf.
