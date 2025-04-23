#!/bin/bash

echo -n "Enter a string: "
read str

temp=$(echo "$str" | tr 'a-z' 'A-Z')

echo "The case-changed string is: $temp"
