import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=65 lines=20')
##############################tempereture analyzer########################################

temps=[35, 28, 40, 31, 30, 45, 50]
count= int(0)
highest=int(0)
freezing=32 #freezing temp in farenheight

for c in temps:
    if c >highest:
        highest=c
    if c <freezing:
        count+=1
        
numbers=["none", "one",  "two", "three", "four", "five", "six", "seven"]
print(f"there were {numbers[count]} freezing days. the weekly high was", end= " ")
print(highest)
