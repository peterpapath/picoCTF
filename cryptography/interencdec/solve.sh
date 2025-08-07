#!/usr/bin/bash

# Decrypt the flag
cat enc_flag | base64 -d | cut -d "'" -f2 | base64 -d | python3 -c "import sys; print(''.join([chr((ord(c)-65+19)%26+65) if c.isupper() else chr((ord(c)-97+19)%26+97) if c.islower() else c for c in sys.stdin.read()]))"
