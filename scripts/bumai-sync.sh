#!/bin/bash
# REPO_PATH, ONEDRIVE_DAGBRIEFINGS, ONEDRIVE_WEEKOVERZICHTEN worden
# als EnvironmentVariables meegegeven door de LaunchAgent plist.
LOG="/tmp/bumai-sync.log"

echo "$(date): Sync gestart" >> "$LOG"

cd "$REPO_PATH" \
  && git fetch origin main \
  && git checkout main \
  && git reset --hard origin/main >> "$LOG" 2>&1

LATEST_DAG=$(ls "$REPO_PATH/briefings/ai-briefing-"*.md 2>/dev/null | sort | tail -1)
if [ -n "$LATEST_DAG" ]; then
  cp "$LATEST_DAG" "$ONEDRIVE_DAGBRIEFINGS/"
  echo "$(date): Gekopieerd dagbriefing: $(basename "$LATEST_DAG")" >> "$LOG"
fi

LATEST_WEEK=$(ls "$REPO_PATH/briefings/weekoverzichten/ai-weekoverzicht-"*.md 2>/dev/null | sort | tail -1)
if [ -n "$LATEST_WEEK" ]; then
  cp "$LATEST_WEEK" "$ONEDRIVE_WEEKOVERZICHTEN/"
  echo "$(date): Gekopieerd weekoverzicht: $(basename "$LATEST_WEEK")" >> "$LOG"
fi
