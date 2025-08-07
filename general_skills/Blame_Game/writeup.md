# ANALYSIS
This challenge gives us a python script, and a git folder. From ther description, we notice that the flag has to do with the person that breaks the code.  
  

# SOLUTION
To solve this challenge we use the command `git blame <file_name>`. This command gives us the commit where the specific file is broken. So we use `git blame message.py` and the flag is the authors name.  
  

* Flag: picoCTF{@sk_th3_1nt3rn_ea346835}
