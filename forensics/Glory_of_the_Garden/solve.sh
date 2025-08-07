#!/usr/bin/bash

# Get the flag
strings garden.jpg | grep -oE "picoCTF{.*?}" --color=none