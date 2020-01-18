import re 
passwd = input()
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
pat = re.compile(reg) 				 
mat = re.search(pat, passwd)  
if mat:
    print("Password is valid.")
else:
    print("Password invalid !!") 
 
