import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################inventory manager########################################

inventory = {"apples": 5, "bananas": 12, "oranges": 0}

print(inventory)
print("")
shipment = ["apples", "oranges", "apples", "apples"]

for i in shipment:
    if i in inventory:
        inventory[i]+=1
        print(f"one {i[:-1]} was added to the inventory") #singular noun
print("")
print(inventory)