#!/usr/bin/bash

# Get the flag
unzip -q challenge.zip && cd drop-in && git blame message.py | grep -oE "picoCTF{.*?}" --color=none