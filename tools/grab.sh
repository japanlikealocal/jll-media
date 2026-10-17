#!/bin/bash
# usage: grab.sh URL -> prints ID|title|channel|duration|date|chars, writes ID.txt
ID=$(echo "$1" | sed -E "s#.*(youtu\.be/|v=|shorts/)([A-Za-z0-9_-]{11}).*#\2#"); U="https://www.youtube.com/watch?v=$ID"; cd /home/claude/yt
for c in default android web_embedded tv; do
  A=(); [ "$c" != default ] && A=(--extractor-args "youtube:player_client=$c")
  META=$(./yt-dlp "${A[@]}" --skip-download --print "%(id)s|%(title)s|%(channel)s|%(duration_string)s|%(upload_date)s" "$U" 2>/dev/null | head -1)
  ./yt-dlp "${A[@]}" --skip-download --write-auto-subs --write-subs --sub-langs "ja,ja-orig,en" --sub-format vtt -o "%(id)s.%(ext)s" "$U" >/dev/null 2>&1
  V=$(ls $ID.ja.vtt $ID.ja-orig.vtt $ID.en.vtt 2>/dev/null | head -1)
  [ -n "$V" ] && break
done
[ -n "$V" ] && python3 vtt2txt.py "$V" > $ID.txt
echo "$META|chars=$(wc -m < $ID.txt 2>/dev/null)"
