import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################Replace Elements with Greatest Element on Right Side########################################

def rightMaxReplacement(arr):
    max_so_far=-1
    for i in range(-1,-len(arr)-1,-1):
        tmp=arr[i]
        arr[i]=max_so_far
        if tmp>max_so_far:
            max_so_far=tmp

    return arr


print(rightMaxReplacement([17, 18, 5, 4, 6, 1]))