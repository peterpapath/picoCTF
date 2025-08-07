#!/usr/bin/env python3

# Get the flag
hex_str = "70"
ascii_char = chr(int(hex_str, 16))
print('picoCTF{' + ascii_char + '}')