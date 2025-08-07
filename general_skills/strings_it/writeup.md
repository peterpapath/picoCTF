# ANALYSIS
This challenge gives us an ELF file, which has a flag.  
  

# SOLUTION
When we try to run it, we don't get a flag. So we use a command named `strings`, to et all the printabl characters from the file and pipe it to a grep to only get the flag. Full command: `strings <file> | grep -oE picoCTF{.*?}`.  
  


* Flag: picoCTF{5tRIng5_1T_827aee91}
