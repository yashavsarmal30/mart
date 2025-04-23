#!/bin/bash

echo -n "Enter the string: "
read str

len=${#str}
temp=""

for (( i=$len-1; i>=0; i-- ))
do
  temp="$temp${str:$i:1}"
done

echo "The reversed string is: $temp"
