import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################remove element########################################

def removeElements(nums,val):
    k=0
    for i in range(len(nums)):
        if not nums[i]==val:
            tmp=nums[k]
            nums[k]=nums[i]
            nums[i]=tmp
            k+=1


    
    return k, nums


print(removeElements([3, 2, 2, 3], 3))
print(removeElements([0, 1, 2, 2, 3, 0, 4, 2], 2))