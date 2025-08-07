# ANALYSIS
This challenge gives us a file with an encrypted text. We are also given the decryption algorithm.  
  

# SOLUTION
To solve the challenge, we need to make a decryption script.  
  
```python3
encoded = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽'
flag = ''

for ch in encoded:
    val = ord(ch)
    flag += chr((val >> 8) & 0xFF)
    flag += chr(val & 0xFF)

print(flag)

```
  

* Flag: picoCTF{16_bits_inst34d_of_8_e141a0f7}
