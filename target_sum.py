import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################The target sum########################################

def  hasTargetSum(nums, target):
    for i in nums:
        second_number=target-i
        if second_number in nums:
            nums0=nums.copy()
            nums0.remove(i)
            if second_number in nums0:
                return True
            
    return False




def  hasTargetSum0(nums, target):
    for i in nums:
        second_number=target-i
        if second_number in nums and (second_number !=i or nums.count(second_number)>1):
            return True
            
    return False






print(hasTargetSum([1, 4, 6, 10],10))
print(hasTargetSum([3, 2, 4],6))
print(hasTargetSum([1, 2, 3],7))