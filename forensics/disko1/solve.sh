#!/usr/bin/bash

gunzip disk*
strings disko-1.dd | grep -oE picoCTF{.*?} --color=none