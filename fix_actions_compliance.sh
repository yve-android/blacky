#!/usr/bin/env bash
set -euo pipefail

WORKFLOW_DIR=".github/workflows"
BACKUP_DIR=".github/workflows_backup_$(date +%Y%m%d_%H%M%S)"

echo "🚦 Actions Compliance Fix gestartet"
echo "📁 Workflows: $WORKFLOW_DIR"
echo "🗂 Backup:    $BACKUP_DIR"
echo

mkdir -p "$BACKUP_DIR"
cp -r "$WORKFLOW_DIR"/*.yml "$BACKUP_DIR"/ 2>/dev/null || true

declare -A ACTION_SHAS=(
  ["actions/checkout@v4"]="actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11"
  ["actions/setup-python@v5"]="actions/setup-python@82c7e631bb3cdc910f68e0081d67478d79c6982d"
  ["actions/cache@v4"]="actions/cache@0c45773b623bea8c8e75f6c82b208c3cf94ea4f9"
  ["actions/upload-artifact@v4"]="actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3"
)

FOUND=0

for file in "$WORKFLOW_DIR"/*.yml; do
  echo "🔎 Prüfe $file"
  for action in "${!ACTION_SHAS[@]}"; do
    if grep -q "$action" "$file"; then
      echo "  ❌ Ersetze $action"
      sed -i "s|$action|${ACTION_SHAS[$action]}|g" "$file"
      FOUND=1
    fi
  done
done

echo
if [[ "$FOUND" -eq 1 ]]; then
  echo "✅ Fix abgeschlossen. Änderungen vorgenommen."
  echo "➡️  Jetzt ausführen:"
  echo "   git diff"
  echo "   git commit -am \"chore(ci): pin GitHub Actions to SHAs\""
  echo "   git push"
else
  echo "🟢 Keine verbotenen Actions gefunden. Alles sauber."
fi
