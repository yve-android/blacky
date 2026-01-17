#!/data/data/com.termux/files/usr/bin/bash
SRC="$HOME/lucy"
OUT="/storage/emulated/0/lucy_backup_$(date +%Y%m%d).zip"

[ ! -d "$SRC" ] && echo "❌ Lucy nicht gefunden" && exit 0

cd "$HOME"
zip -r "$OUT" lucy -x "*/.gradle/*" "*/.buildozer/*"
echo "🎧 Lucy Backup fertig → $OUT"
