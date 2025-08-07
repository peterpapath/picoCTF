#!/usr/bin/bash

# Get the flag
unzip -q challenge.zip && cd drop-in && git log | grep -oE "picoCTF{.*?}" --color=none