import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################maximum average subarray########################################

def maxAvgSubarray(nums,k):
    max_sum=sum([nums[:k]])
    max_avg=float(max_sum)/k

    for i in range(k,len(nums,1)):
        curr_sum=max_sum-nums[i-k]+nums[k]
        curr_avg=float(curr_sum)/k

        if curr_avg>max_avg:
            max_avg=curr_avg
    return

print(maxAvgSubarray([1, 12, -5, -6, 50, 3],4))
print(maxAvgSubarray([5],1))
print(maxAvgSubarray([0, 4, 0, 3, 2],2))


#[0, 4, 0, 3, 2, 12, -5, -6, 50, 3]
#0   1  2  3  4   5   6   7   8  9