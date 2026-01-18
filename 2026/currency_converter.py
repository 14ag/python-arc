import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################currency converter########################################

print(" converts EUR/USD 1.08 ")
def convertCurrency(amount,rate):
    money= float(amount*rate-2)
    if money < 0 : money=0 
    return money

print(convertCurrency(500,0.92))