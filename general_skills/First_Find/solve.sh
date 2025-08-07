#!/usr/bin/bash

# Get the flag
unzip -q files.zip && file=$(find files | grep "uber-secret.txt") && cat $file
