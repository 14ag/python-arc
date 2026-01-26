import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################Single Number########################################

def findSingleNumber(nums):
    result=0
    
    for num in nums:
        result=result ^ num

    return result

print(findSingleNumber([2, 2, 1]))
print(findSingleNumber([ 1, 2, 4, 1, 2]))
print(findSingleNumber([1]))