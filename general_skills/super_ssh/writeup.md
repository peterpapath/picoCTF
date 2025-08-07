# ANALYSIS
This challenge gives us info for an ssh connection.  
  

# SOLUTION
The *ssh* command to connect to a remote server is: `ssh <username>@<ipaddress> -p <port>`
  
So we have:
```bash
ssh ctf-player@titan.picoctf.net -p 60022
```
  
Give the correct password and the flag is ours.
  

* Flag: picoCTF{s3cur3_c0nn3ct10n_5d09a462}
