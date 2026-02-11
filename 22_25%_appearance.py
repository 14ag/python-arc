import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################Element Appearing More Than 25% In Sorted Array########################################

def return25appearance(arr):
    mode={}
    for i in arr:
        if i not in mode:
            mode[i]=1
        else:
            mode[i]+=1
    
    for key, value in mode.items():
        if float(value/len(arr))>0.25:
            return key

print(return25appearance([1,2,2,6,6,6,6,7,10]))
print(return25appearance([1,1]))
print(return25appearance([1,2,3,3]))