import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################Check if All Characters Have Equal Occurrences########################################

def checkIfCharOccurrencesEqual(s):
    obj={}
    for c in s:
        if c in obj:
            obj[c]+=1
        else:
            obj[c]=1
    
    for value in obj.values():
        if value!=obj[s[0]]:
            return False

    return True


print(checkIfCharOccurrencesEqual("abacbc"))
print(checkIfCharOccurrencesEqual("aaabb"))
print(checkIfCharOccurrencesEqual("abcde"))