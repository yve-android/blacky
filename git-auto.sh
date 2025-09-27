#!/bin/bash
# Git Auto Commit & Push

# Prüfen, ob wir im richtigen Verzeichnis sind
if [ ! -d ".git" ]; then
    echo "⚠️ Kein Git-Repo hier! Bitte in dein Projektverzeichnis wechseln."
    exit 1
fi

# Alle Änderungen hinzufügen
git add .

# Commit erstellen (mit aktuellem Zeitstempel, falls keine Nachricht)
COMMIT_MSG=${1:-"Update $(date '+%Y-%m-%d %H:%M:%S')"}
git commit -m "$COMMIT_MSG"

# Push auf main
git push origin main

echo "✅ Änderungen erfolgreich gepusht!"
