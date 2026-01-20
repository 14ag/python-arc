import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################duplicate finder########################################

def checkForDuplicates(arr0):
    if len(arr0)==len(set(arr0)):
        return False
    else:
        return True
    
print(checkForDuplicates([1, 2, 3, 1]))
print(checkForDuplicates([1, 2, 3, 4]))
print(checkForDuplicates([1, 1, 1, 3, 3, 4]))