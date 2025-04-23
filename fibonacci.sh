#!/bin/bash

echo -n "Enter the limit: "
read n
echo "The Fibonacci series:"

b=0
c=1

if [ $n -ge 2 ]; then
  echo -n "$b $c "
  for ((i=2; i<n; i++))
  do
    a=$((b + c))
    echo -n "$a "
    b=$c
    c=$a
  done
  echo
else
  echo "$b"
fi
