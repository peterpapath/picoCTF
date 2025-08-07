#!/usr/bin/bash


unzip -q challenge.zip && cd drop-in && git diff feature/part-3 feature/part-2 feature/part-1 | grep 'print(' | sed -E 's/.*print\("([^"]+).*/\1/' | tr -d '\n' | grep -oE "picoCTF{.*?}" --color=none