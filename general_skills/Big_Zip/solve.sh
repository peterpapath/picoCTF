#!/usr/bin/bash

# Get the flag
unzip -q big-zip-files.zip && grep -RoE "picoCTF{.*?}" --color=none | cut -d ":" -f2