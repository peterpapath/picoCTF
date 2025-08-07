#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
from pwn import *
context.log_level = 'error'

HOST = 'verbal-sleep.picoctf.net'
PORT = 58750


def decrypt(N, ciphertext):
	# Set the values
	e = 65537
	q = N // 2
	phi_N = q - 1

	# Make the decryption
	d = pow(e, -1, phi_N)
	m = pow(ciphertext, d, N)
	flag = long_to_bytes(m)

	return flag


def main():
	# Connect to the server and get the values
	p = remote(HOST, PORT)
	p.recvuntil(b"N: ")
	N = int(p.recvline().decode('utf-8').strip())

	p.recvuntil(b"cyphertext: ")
	ciphertext = int(p.recvline().decode('utf-8').strip())

	p.close()

	flag_output = decrypt(N, ciphertext)
	match = re.search(r'picoCTF\{.*?\}', flag_output.decode())
	if match:
		flag = match.group(0)
		print(flag)
	else:
		print("Flag not found.")


if __name__ == "__main__":
	main()