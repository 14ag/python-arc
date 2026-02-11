import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################sort array by parity########################################

def sortByParity(nums):
    return [i for i in nums if i%2==0] + [i for i in nums if i%2!=0]

print(sortByParity([3, 1, 2, 4]))
print(sortByParity([0]))
print(sortByParity([1, 2, 3, 4, 5, 6]))