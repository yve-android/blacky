#!/data/data/com.termux/files/usr/bin/bash
BASE="$HOME/blacky"
MOD="$BASE/modules"

case "$1" in
  dashboard) bash "$MOD/dashboard.sh" ;;
  dedupe) bash "$MOD/dedupe.sh" ;;
  lucy-backup) bash "$MOD/lucy_backup.sh" ;;
  *) echo "Usage: blacky {dashboard|dedupe|lucy-backup}" ;;
esac
