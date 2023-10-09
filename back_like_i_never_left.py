import os
os.system('cls')
os.system('prompt $G')

# # Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

# # The functions:

# # are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
# # take one argument (the value corresponding to their names)
# # Complete the code in the editor and run it to check whether your output is the same as ours.

# # Here is some information to help you:

# # 1 American mile = 1609.344 metres;
# # 1 American gallon = 3.785411784 litres
# # mpg lp100k

# def liters_100km_to_miles_gallon(liters):
#     # get miles
#     m=100/1.609344
#     # get gallons
#     g=liters/3.785411784
#     # ans
#     a=1/g*m
#     return a


# def miles_gallon_to_liters_100km(miles):
#     # get km
#     k=miles*1.609344
#     # get liters
#     l=1*3.785411784
#     # ans
#     a=100/k*l
#     return a

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))


# ==========================================================================================================================

# #def check palindrome
# def p(x):
#     y=[]
#     for i in x:
#         y.append(i)
#     if len(y)%2==0:
#         n=-1
#         for j in range(int(len(y)/2)):
#             if y[j]==y[n]:
#                 j+=1
#                 n-=1
#             else:
#                 return False
#         return True
#     else:
#         n=-1
#         for j in range(int(len(y)//2)):
#             if y[j]==y[n]:
#                 j+=1
#                 n-=1
#             else:
#                 return False
#         return True
# print(p("woow"))
# print(p("phil"))
# print(p("12321"))
# print(p("12324"))


# ===============================================================================
#def check_duplicates
def p(x):
    y=[]
    for i in x:
        y.append(i)
    for j in y:
        z=y.count(j)
        if z>1:
            return True
    return False

print(p("woow"))
print(p("phil"))



















