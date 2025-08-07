# ANALYSIS
This challenge gives us a file, from which we have to obtain a flag. We can download it to our system and analyze it.

# SOLUTION
The file is in a compressed format, so we have to decompress it with th command `gunzip <filename>`. After that we get a disk file.
We can get the flag with the tool called `strings`. We pipe it to a grep command to get only the flag.

![](assets/solve.png)


* Flag: picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
