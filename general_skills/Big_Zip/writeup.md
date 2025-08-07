# ANALYSIS
This challenge gives a big zip file, from which we have to extract the flag.  
  

# SOLUTION
To get the flag we use the command `grep -R .`, which gives us the contents of the files inside a folder. We can pipe this command to another grep to get the flag, `grep -R . | grep picoCTF`.  
  

* Flag: picoCTF{gr3p_15_m4g1c_ef8790dc}
