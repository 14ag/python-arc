import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################can place flowers########################################

def canPlaceFlowers(flowerbed,n):
    for i in range(-len(flowerbed),0,1):
        if flowerbed[i]==0 and n>0:
            if i> -len(flowerbed):
                if i< -1:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        n-=1
                else:
                    if flowerbed[i-1]==0:
                        n-=1
            else:
                if flowerbed[i+1]==0:
                    n-=1

    if n>0:
        return False
    else:
        return True


print(canPlaceFlowers([1, 0, 0, 0, 1],1))
print(canPlaceFlowers([1, 0, 0, 0, 1],2))
print(canPlaceFlowers([0, 0, 1],1))