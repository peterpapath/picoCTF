#!/usr/bin/bash

sshpass -p '1db87a14' ssh \
    -o StrictHostKeyChecking=no \
    -o UserKnownHostsFile=/dev/null \
    -p 56566 ctf-player@rhea.picoctf.net '
    cd drop-in/
    file=$(sha256sum ./files/* | grep "55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a" | awk "{print \$2}")
    ./decrypt.sh "$file" | grep -o "picoCTF{.*}"
' 2>/dev/null


# Change the password and server host and port.