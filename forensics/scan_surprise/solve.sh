#!/usr/bin/bash

# Get the flag from the downloaded zip file
unzip -oq challenge.zip
zbarimg --quiet --raw home/ctf-player/drop-in/flag.png