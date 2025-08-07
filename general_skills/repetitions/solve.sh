#!/usr/bin/bash

# Decrypt the flag
cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
