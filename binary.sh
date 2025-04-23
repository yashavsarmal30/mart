#!/bin/bash

echo "Enter array limit"
read limit

echo "Enter elements (in sorted order)"
for (( i=0; i<limit; i++ ))
do
  read arr[i]
done

echo "Enter key element to search"
read key

low=0
high=$((limit - 1))
found=0

while [ $low -le $high ]
do
  mid=$(((low + high) / 2))
  if [ ${arr[mid]} -eq $key ]; then
    found=1
    break
  elif [ $key -lt ${arr[mid]} ]; then
    high=$((mid - 1))
  else
    low=$((mid + 1))
  fi
done

if [ $found -eq 1 ]; then
  echo "Successful search: $key found at position $((mid + 1))"
else
  echo "Unsuccessful search: $key not found"
fi
