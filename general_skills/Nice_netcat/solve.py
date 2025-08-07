#!/usr/bin/env python3

from pwn import *
context.log_level = 'error'


HOST = 'mercury.picoctf.net'
PORT = 43239
p = remote(HOST, PORT)

    
def main():
    chars = []

    for i in range(42):
        line = p.recvline()
        num = int(line.strip())
        chars.append(chr(num))

    flag = ''.join(chars)
    print(flag)

if __name__ == '__main__':
    main()