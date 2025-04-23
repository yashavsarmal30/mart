#!/bin/bash

echo "Enter a word:"
read word
echo "Enter the filename:"
read file

if [ ! -f "$file" ]; then
  echo "File not found!"
  exit 1
fi

nol=$(grep -c "$word" "$file")

echo "$nol times '$word' present in the $file"
