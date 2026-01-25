import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################find the lone survivor########################################

nums = [2, 4, 6, 2, 4]
frequency_map= {}

for num in nums:
    if not num in frequency_map:
        frequency_map[num] = 1
    else:
        frequency_map[num] +=1

for key, value in frequency_map.items():
    if value==1:
        print(key)
        break
