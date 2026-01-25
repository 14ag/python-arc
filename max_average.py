import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################maximum average subarray########################################

def maxAvgSubarray(nums,k):
    sum0=sum(nums[:k])
    max_avg=float(sum0)/k

    for i in range(k,len(nums)):
        sum0=sum0-nums[i-k]+nums[i]
        
        curr_avg=float(sum0)/k

        if curr_avg >max_avg:
            max_avg=curr_avg

    return max_avg

print(maxAvgSubarray([1, 12, -5, -6, 50, 3],4))

print(maxAvgSubarray([5],1))

print(maxAvgSubarray([0, 4, 0, 3, 2],2))

