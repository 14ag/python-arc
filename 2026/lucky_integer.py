import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################find lucky integer########################################

def findLuckyInteger(arr):
    largest_lucky=-1
    frequency={}
    for i in arr:
        if not i in frequency:
            frequency[i]=1
        elif i in frequency:
            frequency[i]+=1
   # print(frequency)

    for key,value in frequency.items():
        if key==value and key>largest_lucky:
            largest_lucky=key
            
    
    return largest_lucky
        


print(findLuckyInteger([2, 2, 3, 4]))
print(findLuckyInteger([1, 2, 2, 3, 3, 3]))
print(findLuckyInteger([2, 2, 2, 3, 3]))