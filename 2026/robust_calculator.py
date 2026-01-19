import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################robust calculator########################################

print("your first number will be divided by the second one")

a = int(input("input the first number: "))
b = int(input("input the second number: "))


def safeDivide(a,b):
    try:
        result=a/b

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except TypeError:
        print("Error: Inputs must be numbers.")

    except:
        print("something went wrong")

    else:
        print(f"result is {result}")
        return result



safeDivide(a,b)

