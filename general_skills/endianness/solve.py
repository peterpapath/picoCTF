#!/usr/bin/env python3

from pwn import *
context.log_level = 'error'

HOST = 'titan.picoctf.net'
PORT = 60805


def big_endian(word):
	word_bytes = word.encode('ascii')  # or 'utf-8' if needed

	# Big endian hex
	big_endian_hex = word_bytes.hex()

	return big_endian_hex


def little_endian(word):
	word_bytes = word.encode('ascii')  # or 'utf-8' if needed

	# Little endian hex
	little_endian_hex = word_bytes[::-1].hex()

	return little_endian_hex



def main():
	p = remote(HOST, PORT)
	p.recvuntil(b"Word: ")
	word = 	p.recvline().decode("UTF-8").strip()

	# Little Endian
	little_endian_hex = little_endian(word)
	p.sendlineafter(b"representation: ", little_endian_hex.encode())

	# Big Endian
	big_endian_hex = big_endian(word)
	p.sendlineafter(b"representation: ", big_endian_hex.encode())

	# Get the flag
	p.recvuntil(b"is: ")
	flag = p.recvline().decode("UTF-8").strip()
	print(flag)
	p.close()



if __name__ == '__main__':
	main()