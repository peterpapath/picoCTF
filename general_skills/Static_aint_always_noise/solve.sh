#!/usr/bin/bash

# Get the flag
./ltdis.sh static | grep "something"
cat static.ltdis.strings.txt | grep -oE "picoCTF{.*?}" --color=none