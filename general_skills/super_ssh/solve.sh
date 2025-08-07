#!/usr/bin/bash

# Get the flag from the remote server
sshpass -p '6dd28e9b' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 54141 ctf-player@titan.picoctf.net 2>/dev/null | grep -oE "picoCTF{.*?}" --color=none