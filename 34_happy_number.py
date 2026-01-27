import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################happy number########################################

def isHappyNumber(n):
    my_set=set(["x"])

    while True:
        digit4=n//1000
        digit3=(n-(digit4*1000))//100
        digit2=(n-(digit3*100))//10
        digit1=n%10

        #print(n,digit4,digit3,digit2,digit1 )
        n=(digit4**2)+(digit3**2)+(digit2**2)+(digit1**2)

        if n==1:
            return True
        else:
            if n in my_set:
                return False
            else:
                my_set.add(n)


   
        


   
    

print(isHappyNumber(19))
print(isHappyNumber(2))