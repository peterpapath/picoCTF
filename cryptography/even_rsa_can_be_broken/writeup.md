# ANALYSIS
This challenge consists of an easy RSA algorithm
  

# SOLUTION
After connecting to the server we get the values for N, e and the ciphertext. We pass them to a decryption program and we get the flag.
  

```python
from Crypto.Util.number import long_to_bytes

N = <given_even_N>
e = 65537

q = N // 2
phi_N = q - 1
d = pow(e, -1, phi_N)

ciphertext = <given_ciphertext>
m = pow(ciphertext, d, N)
flag = long_to_bytes(m)
print(flag)
```

  
* Flag: picoCTF{tw0_1$_pr!m33991588e}
