#!/usr/bin/env python3
import subprocess
import os
import tempfile
from pwn import *
context.log_level = 'error'

HOST= "verbal-sleep.picoctf.net"
PORT= 53299

p = remote(HOST, PORT)


# MD5 crack function
def crack_md5_hash(md5_hash: str, username: str = "user") -> str | None:
    # Create a temporary file to store the hash in john format: username:hash
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp_hash_file:
        tmp_hash_file.write(f"{username}:{md5_hash}\n")
        tmp_hash_file_path = tmp_hash_file.name

    # Remove john.pot cache to ensure clean run
    john_pot = os.path.expanduser("~/.john/john.pot")
    if os.path.exists(john_pot):
        os.remove(john_pot)

    # Run john (suppress stdout and stderr)
    subprocess.run(
        ["john", tmp_hash_file_path, "--wordlist=/usr/share/wordlists/rockyou.txt", "--format=Raw-MD5"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Run john --show to get the result
    result = subprocess.run(
        ["john", tmp_hash_file_path, "--show", "--format=Raw-MD5"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    # Parse output to extract the cracked password
    password = None
    lines = result.stdout.strip().splitlines()
    for line in lines:
        if ":" in line and not line.startswith(" "):
            _, password = line.split(":", 1)
            password = password.strip()
            break

    # Clean up the temporary hash file
    os.remove(tmp_hash_file_path)

    return password



# SHA1 crack function
def crack_sha1_hash(sha1_hash: str, username: str = "user") -> str | None:
    # Create a temporary file to store the hash in john format: username:hash
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp_hash_file:
        tmp_hash_file.write(f"{username}:{sha1_hash}\n")
        tmp_hash_file_path = tmp_hash_file.name

    # Remove john.pot cache to ensure clean run
    john_pot = os.path.expanduser("~/.john/john.pot")
    if os.path.exists(john_pot):
        os.remove(john_pot)

    # Run john (suppress stdout and stderr)
    subprocess.run(
        ["john", tmp_hash_file_path, "--wordlist=/usr/share/wordlists/rockyou.txt", "--format=Raw-SHA1"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Run john --show to get the result
    result = subprocess.run(
        ["john", tmp_hash_file_path, "--show", "--format=Raw-SHA1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    # Parse output to extract the cracked password
    password = None
    lines = result.stdout.strip().splitlines()
    for line in lines:
        if ":" in line and not line.startswith(" "):
            _, password = line.split(":", 1)
            password = password.strip()
            break

    # Clean up the temporary hash file
    os.remove(tmp_hash_file_path)

    return password



# SHA256 crack function
def crack_sha256_hash(sha256_hash: str, username: str = "user") -> str | None:
    # Create a temporary file to store the hash in john format: username:hash
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp_hash_file:
        tmp_hash_file.write(f"{username}:{sha256_hash}\n")
        tmp_hash_file_path = tmp_hash_file.name

    # Remove john.pot cache to ensure clean run
    john_pot = os.path.expanduser("~/.john/john.pot")
    if os.path.exists(john_pot):
        os.remove(john_pot)

    # Run john (suppress stdout and stderr)
    subprocess.run(
        ["john", tmp_hash_file_path, "--wordlist=/usr/share/wordlists/rockyou.txt", "--format=Raw-SHA256"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Run john --show to get the result
    result = subprocess.run(
        ["john", tmp_hash_file_path, "--show", "--format=Raw-SHA256"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    # Parse output to extract the cracked password
    password = None
    lines = result.stdout.strip().splitlines()
    for line in lines:
        if ":" in line and not line.startswith(" "):
            _, password = line.split(":", 1)
            password = password.strip()
            break

    # Clean up the temporary hash file
    os.remove(tmp_hash_file_path)

    return password




def main():
    # MD5 hash decrypt
    p.recvuntil(b"hash: ")
    md5_hash = p.recvline().decode('utf-8').strip()
    cracked_1 = crack_md5_hash(md5_hash)
    if cracked_1 is None:
        print("[-] Failed to crack md5 hash.")
        return
    p.sendlineafter(b"identified hash: ", cracked_1.encode())


    # SHA1 hash decrypt
    p.recvuntil(b"hash: ")
    sha1_hash = p.recvline().decode('utf-8').strip()
    cracked_2 = crack_sha1_hash(sha1_hash)
    if cracked_2 is None:
        print("[-] Failed to crack sha1 hash.")
        return
    p.sendlineafter(b"identified hash: ", cracked_2.encode())


    # SHA256 hash decrypt
    p.recvuntil(b"hash: ")
    sha256_hash = p.recvline().decode('utf-8').strip()
    cracked_3 = crack_sha256_hash(sha256_hash)
    if cracked_3 is None:
        print("[-] Failed to crack sha256 hash.")
        return
    p.sendlineafter(b"identified hash: ", cracked_3.encode())
    

    # Get the flag
    p.recvuntil(b"is: ")
    flag = p.recvline().decode('utf-8').strip()
    print(flag)


    # Close the connection
    p.close()



if __name__ == "__main__":
    main()