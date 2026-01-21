import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################move zeros########################################

nums = [0, 1, 0, 3, 12]


def moveZeros(arr0):
    count=0
    non_zero=[]
    for i in arr0:
        if i ==0:
            count+=1
            continue
        non_zero.append(i)
    non_zero+=[0]*count
    return non_zero

print(moveZeros(nums))
