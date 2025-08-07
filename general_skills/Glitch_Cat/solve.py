#!/usr/bin/env python3

from pwn import *
context.log_level = 'error'

HOST = 'saturn.picoctf.net'
PORT = 57412


def main():
	# Connecto to the server
	p = remote(HOST, PORT)

	flag = p.recvline().decode().strip()
	flag_final = eval(flag)
	p.close()
	print(flag_final)


if __name__ == '__main__':
	main()