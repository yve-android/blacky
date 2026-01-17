#!/data/data/com.termux/files/usr/bin/bash
USED=$(df -h "$HOME" | tail -n1 | awk '{print $5}' | tr -d '%')
BAR=$((USED/5))
printf "📊 BLACKY DASHBOARD\n["
for i in $(seq 1 20); do
  [ "$i" -le "$BAR" ] && printf "█" || printf " "
done
echo "] $USED%"
du -sh "$HOME/blacky" 2>/dev/null
