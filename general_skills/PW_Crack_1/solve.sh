#!/usr/bin/bash

# Run on the same dir as the given files.

# Get the flag
echo "691d" | python3 level1.py | grep -oE "picoCTF{.*?}" --color=none