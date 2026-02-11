import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################intersection of two arrays########################################

def intersectionFinder(nums0,nums1):
    return list(set(nums0).intersection(set(nums1)))

print(intersectionFinder([1, 2, 2, 1],[2, 2]))
print(intersectionFinder([4, 9, 5],[9, 4, 9, 8, 4]))
print(intersectionFinder([1, 2, 3],[4, 5, 6]))
