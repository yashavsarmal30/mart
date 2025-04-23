#!/bin/bash

# Displaying lines 1 and 2 from the /etc/passwd file
echo "Line Addressing"
sed -n '1,2p' /etc/passwd

# Displaying lines 5 to 6, then 7 to 9 using line addressing
echo "Multiple Line Addressing"
sed -n '5,6p;7,9p' /etc/passwd

# Searching and printing lines containing the string 'jnec' from the /etc/passwd file
echo "Context Addressing"
sed -n '/jnec/p' /etc/passwd
