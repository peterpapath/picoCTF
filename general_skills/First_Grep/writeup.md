# ANALYSIS
This challenge gives us a file, from which we have to extract a flag.  
  

# SOLUTION
The problem is that its content is very large. Since we know that the flag format is **picoCTF{...}**, we can use a tool called `grep` to only get the flag. Command: `grep -RoE picoCTF{.*?} ./file`.  
  

* Flag: picoCTF{grep_is_good_to_find_things_dba08a45}
