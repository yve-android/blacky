#!/data/data/com.termux/files/usr/bin/bash
SRC="$HOME"
DST="$HOME/blacky/data/master"
LOG="$HOME/blacky/logs/dedupe_$(date +%s).log"

declare -A HASHES

find "$SRC" -type f -iname "*blacky*" 2>/dev/null | while read f; do
  h=$(sha256sum "$f" | awk '{print $1}')
  if [[ -n "${HASHES[$h]}" ]]; then
    echo "DUPLICATE: $f == ${HASHES[$h]}" >> "$LOG"
  else
    HASHES[$h]="$f"
    mkdir -p "$DST"
    cp -n "$f" "$DST/" 2>/dev/null || true
  fi
done

echo "🧹 Dedup abgeschlossen → $LOG"
