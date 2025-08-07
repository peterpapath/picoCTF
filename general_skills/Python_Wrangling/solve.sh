#!/usr/bin/bash

# Get the flag
cat pw.txt | python3 ende.py -d flag.txt.en | cut -d ":" -f2