#!/usr/bin/bash

# Get the flag
strings strings | grep -oE picoCTF{.*?} --color=none