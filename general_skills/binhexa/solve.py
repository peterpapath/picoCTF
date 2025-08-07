#!/usr/bin/env python3

from pwn import *
context.log_level = 'error'
import re

HOST = 'titan.picoctf.net'
PORT = 60625                  # Change these if needed


def main():
    p = remote(HOST, PORT)

    # Get the numbers
    p.recvuntil(b"1: ")
    number1 = p.recvline().decode("UTF-8").strip()
    a = int(number1, 2)
    p.recvuntil(b"2: ")
    number2 = p.recvline().decode("UTF-8").strip()
    b = int(number2, 2)


    for i in range(6):

        # Get the operation
        p.recvuntil(f"Operation {i+1}: ".encode())
        operator = p.recvline().decode("UTF-8").strip().strip("'")

        if (operator == "|"):
            p.recvuntil(b"result: ")
            result = a | b
            formated_result = format(result, '08b')
            p.send(formated_result.encode())
            p.send(b"\n")

        elif (operator == "&"):
            p.recvuntil(b"result: ")
            result = a & b
            formated_result = format(result, '08b')
            p.send(formated_result.encode())
            p.send(b"\n")

        elif (operator == "+"):
            p.recvuntil(b"result: ")
            result = a + b
            formated_result = format(result, '08b')
            p.send(formated_result.encode())
            p.send(b"\n")

        elif (operator == "-"):
            p.recvuntil(b"result: ")
            result = a - b
            formated_result = format(result, '08b')
            p.send(formated_result.encode())
            p.send(b"\n")

        elif (operator == "*"):
            p.recvuntil(b"result: ")
            result = a * b
            formated_result = format(result, '08b')
            p.send(formated_result.encode())
            p.send(b"\n")

        elif (operator == "<<"):
            line = p.recvline().decode("UTF-8").strip()
            match = re.search(r'Binary Number (\d+) by (\d+) bits', line)
            if match:
                binary_num = int(match.group(1))
                bits = int(match.group(2))
                if (binary_num == 1):
                    binary_num = number1
                elif (binary_num == 2):
                    binary_num = number2
                else:
                    print("Something happened")
                    sys.exit(1)
            else:
                print("Pattern not matched!")
            # Do the shift
            result = int(binary_num, 2) << bits
            formated_result = bin(result)[2:]
            p.send(formated_result.encode())
            p.send(b"\n")


        elif (operator == ">>"):
            line = p.recvline().decode("UTF-8").strip()
            match = re.search(r'Binary Number (\d+) by (\d+) bits', line)
            if match:
                binary_num = int(match.group(1))
                bits = int(match.group(2))
                if (binary_num == 1):
                    binary_num = number1
                elif (binary_num == 2):
                    binary_num = number2
                else:
                    print("Something happened")
                    sys.exit(1)
            else:
                print("Pattern not matched!")
            # Do the shift
            result = int(binary_num, 2) >> bits
            formated_result = bin(result)[2:]
            p.send(formated_result.encode())
            p.send(b"\n")

        if (i == 5):
            p.recvuntil(b"hexadecimal: ")
            hex_result = hex(result)
            p.send(hex_result.encode())
            p.send(b"\n")



    # Get the flag
    p.recvuntil(b"is: ")
    flag = p.recvline().decode("UTF-8").strip()
    print(flag)


    # Close the connection
    p.close()


if __name__ == '__main__':
    main()
