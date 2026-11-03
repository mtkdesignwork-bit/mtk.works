#!/bin/bash
# image-src の HTML を 1220×1240px の PNG にして、出品画像フォルダに書き出す
# 使い方：bash render.sh（-draft 以外の全部）／ bash render.sh base-edit-1（1枚だけ）
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="../出品画像"
mkdir -p "$OUT"
names="$@"
if [ -z "$names" ]; then
  names=$(ls *.html | grep -v -- '-draft' | sed 's/\.html$//')
fi
for n in $names; do
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files \
    --force-device-scale-factor=1 --window-size=1220,1240 --virtual-time-budget=8000 \
    --screenshot="$OUT/$n.png" "file://$PWD/$n.html" >/dev/null 2>&1
  echo "$OUT/$n.png"
done
