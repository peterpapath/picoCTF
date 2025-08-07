#!/usr/bin/bash

# Get the flag
unzip -q challenge.zip && cd drop-in && git checkout 87b85d7dfb839b077678611280fa023d76e017b8 > /dev/null 2>&1 && cat message.txt