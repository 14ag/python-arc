import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################find lucky integer########################################

def findLuckyInteger(arr):
    frequency={}
    for i in arr:
        if arr.count(i)==i:
            frequency[i]=arr.count(i)
            
    if len(frequency)>0:
        return max(frequency)
    else:
        return -1
        



print(findLuckyInteger([2, 2, 3, 4]))
print(findLuckyInteger([1, 2, 2, 3, 3, 3]))
print(findLuckyInteger([2, 2, 2, 3, 3]))