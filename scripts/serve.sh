#!/usr/bin/env zsh
set -euo pipefail

# Tuer tout processus écoutant sur le port 8000
if lsof -i TCP:8000 -sTCP:LISTEN -t >/dev/null; then
  echo "⚠️ Port 8000 occupé, je tue le processus en cours…" 
  lsof -i TCP:8000 -sTCP:LISTEN -t | xargs kill -9
fi

mkdocs serve &

until curl -fs 127.0.0.1:8000/ >/dev/null; do
  sleep 0.2
done

osascript <<EOF
tell application "Firefox"
  open location "http://127.0.0.1:8000/"
  activate
end tell
EOF