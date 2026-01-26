import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################montonic array########################################


def isMonotonicArray(nums):
    tf0=(nums[0] <= nums[-1])

    for i in  range(1,len(nums)):
        tf1=(nums[i-1] <= nums[i])
        #print(i, tf0, tf1)

        if tf1 != tf0 and not (nums[i-1] == nums[i]):
            return False
        
    return True


print(isMonotonicArray([1, 2, 2, 3]))
print(isMonotonicArray([6, 5, 4, 4]))
print(isMonotonicArray([1, 3, 2]))