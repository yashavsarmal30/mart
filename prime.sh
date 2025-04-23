#!/bin/bash

echo "Enter the number"
read n

i=2
while [ $i -lt $n ]
do
  if [ $((n % i)) -eq 0 ]
  then
    break
  fi
  i=$((i + 1))
done

if [ $i -eq $n ]
then
  echo "Prime number"
else
  echo "Not Prime"
fi
