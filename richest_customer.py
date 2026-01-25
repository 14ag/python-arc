import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################richest customer wealth########################################

def accumulate(accounts):
    max_wealth=0
    for i in accounts:
        wealth=sum(i)
        if wealth> max_wealth:
            max_wealth=wealth
    return max_wealth

print(accumulate([[1,2,3],[3,2,1]]))
print(accumulate([[1,5],[7,3],[3,5]]))
print(accumulate([[2,8,7],[7,1,3],[1,9,5]]))