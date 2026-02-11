import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
################################password validator######################################

#vars
ws= " " #whitespace
password= str((input("write a password: ")))

#check the password length
#check if it has a whitespace
if len(password)<8 or ws in password:
    print("invalid password")
else:
    print("password is valid")
