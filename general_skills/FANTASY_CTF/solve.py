#!/usr/bin/env python3
from pwn import *
context.log_level = 'error'

HOST = 'verbal-sleep.picoctf.net'
PORT = 55628

p = remote(HOST, PORT)

def main():
	# Connect and recieve until the prompt
	for i in range(5):
		p.recvuntil(b"---")
		p.recvuntil(b"---")
		p.send(b"\n")

	# Give something to the prompt
	p.sendlineafter(b"> ", b"a")

	# Get to the other prompt
	for i in range(6):
		p.recvuntil(b"---")
		p.recvuntil(b"---")
		p.send(b"\n")

	# Give the value a to the prompt
	p.sendlineafter(b"> ", b"a")

	# End the game
	for i in range(8):
		p.recvuntil(b"---")
		p.recvuntil(b"---")
		p.send(b"\n")

	# Get the flag using its regex
	p.recvuntil(b"4. ")
	line = p.recvline().decode('utf-8').strip()
	match = re.search(r'picoCTF\{.*?\}', line)
	if match:
		flag = match.group(0)
		p.close()
		print(flag)
	else:
		p.close()
		print("Flag not found.")


if __name__ == "__main__":
	main()