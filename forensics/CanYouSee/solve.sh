#!/usr/bin/bash

# Get the flag
unzip -q unknown.zip && exiftool ukn_reality.jpg | grep "Attribution URL" | cut -d ":" -f2 | tr -d " " | base64 -d
