#!/usr/bin/bash

# Run on the same dir as the given files.

# Get the flag
echo "39ce" | python3 level2.py | grep -oE "picoCTF{.*?}" --color=none