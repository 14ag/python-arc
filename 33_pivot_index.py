import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################find pivot index########################################

def findPivotIndex(nums):
    total_sum=sum(nums)
    left_sum=0
    for i in range(len(nums)):
        right_sum=total_sum-left_sum-nums[i]
        if right_sum==left_sum:
            return i
        
        left_sum+=nums[i]

    return -1

print(findPivotIndex([1, 7, 3, 6, 5, 6]))
print(findPivotIndex([1, 2, 3]))
print(findPivotIndex([2, 1, -1]))
