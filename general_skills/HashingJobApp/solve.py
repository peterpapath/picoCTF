#!/usr/bin/env python3

from pwn import *
context.log_level = 'error'
import hashlib

HOST = 'saturn.picoctf.net'
PORT = 58784                 # Change if needed

def main():
    # Connect to the remote bserver
    p = remote(HOST, PORT)
    

    for i in range(3):
        # Get the Word
        p.recvuntil(b"quotes: ")
        word = p.recvline().decode("UTF-8").strip().strip("'")

        # Calculate the hash
        md5_hash = hashlib.md5(word.encode()).hexdigest()

        # Send the hash back to the server
        p.send(md5_hash.encode())
        p.send(b"\n")

    # Get the flag
    p.recvuntil(b"Correct.")
    p.recvline()
    flag = p.recvline().decode("UTF-8").strip()
    p.close()
    print(flag)




if __name__ == '__main__':
    main()