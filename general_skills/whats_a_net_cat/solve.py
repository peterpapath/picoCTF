#!/usr/bin/env python3

from pwn import *
context.log_level = 'error'

# Make the connection
HOST = 'jupiter.challenges.picoctf.org'
PORT = 64287
p = remote(HOST, PORT)

def main():
	# Get the flag
	p.recvline()
	flag = p.recvline().decode().strip()
	print(flag)

if __name__ == '__main__':
	main()