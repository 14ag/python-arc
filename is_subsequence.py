import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################is subsequence########################################

def subsequentCheck(s_string,t_string):
    i=0
    for t in t_string:
        if s_string[i]==t:
            i+=1
        if i==len(s_string):
            return True
        
    return False



print(subsequentCheck("abc","ahbgdc"))
print(subsequentCheck("axc","ahbgdc"))
print(subsequentCheck("ace","abcde"))