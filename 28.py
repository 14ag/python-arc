import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################merge sort array########################################

def sort0(nums1,m,nums2,n):
    p1=-m-1
    p2=-1
    for i in range(-1,-len(nums1)-1,-1):
        print(p1,p2)
        if not p1 < -len(nums1):
            if not p2 < -n:
                if nums2[p2]>nums1[p1]:
                    nums1[i]=nums2[p2]
                    p2-=1
                else:
                    nums1[i]=nums1[p1]
                    p1-=1
            else:
                nums1[i]=nums1[p1]
                p1-=1
        else:
            nums1[i]=nums2[p2]
            p2-=1

    return nums1

print(sort0([4, 5, 6, 0, 0, 0],3,[1, 2, 3],3))