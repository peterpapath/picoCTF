#!/usr/bin/bash

# Get the flag
exiftool cat.jpg | grep License | tr -d " " | cut -d ":" -f2 | base64 -d