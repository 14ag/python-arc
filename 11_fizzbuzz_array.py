import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################fizzbuzz array########################################

#number= input("pick a number, any number: ")
number=30
def fizzBuzz(n):
    n=int(n)+1
    fizzbuzz=[]
    for i in range(1,n):
        if i%15==0:
            fizzbuzz.append("FizzBuzz")
            continue
        if i%5==0:
            fizzbuzz.append("Buzz")
        elif i%3==0:
            fizzbuzz.append("Fizz")
            continue
        else:
            fizzbuzz.append(str(i))
    return fizzbuzz                       

print(fizzBuzz(number))