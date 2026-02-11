import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################palindrome checker########################################

s = "radar"

def isPalindrome(s):
    if len(s)==1 or len(s)==0:
        print("True")
        return True
    if s[0]==s[-1]:
        return isPalindrome(s[1:-1])
    else:
        print("False")
        return False

isPalindrome(s)
