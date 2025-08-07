#!/usr/bin/bash

# Extract the hidden info and get only the flag
zsteg -a red.png |  grep "b1,rgba,lsb,xy" | cut -d "\"" -f2 | cut -d "." -f1 | cut -d "=" -f1 | base64 -d
