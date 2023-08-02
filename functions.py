import os
os.system('cls')
# os.system('prompt $G')


# def message():
#     print("Enter a value: ")
 
# print("We start here.")
# message()
# print("We end here.")



# def x(the):
#     an=int(input("Enter a value: "))
#     print(the+"="+str(an))
#     the=an
# x(the="a")
# x(the="b")
# x(the="c")
# print(an)



# def message(number):
#     print("Enter a number:", number)
 
# number = 1234
# message(1)
# print(number)





# def hello(name): # defining a function
#     print("Hello,", name) # body of the function
 
 
# name = input("Enter your name: ")
 
# hello(name) # calling the function







# def is_year_leap(year):
#     a=year%4==0      # 1 1
#     b=year%100==0    # 0 1
#     c=year%400==0    #   1
#     if (a and not b) or c:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     a=year%4==0      # 1 1
#     b=year%100==0    # 0 1
#     c=year%400==0    #   1
#     m=[i for i in range(1,13)]
#     if month in m:
#         if (a and not b) or c:
#                 d=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         else:
#                 d=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         return d[month]
#     else:
#          return None

def day_of_year(year, month, day):
    m=[i for i in range(1,13)]
    t=day
    d=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month in m:
        if (year%4==0 and not year%100==0) or year%400==0:
            d[2]=29
        for i in range(month):
                t+=d[i]
        return t
    else:
         return None

print(day_of_year(2000, 12, 31))

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print(result, "OK")
#     else:
#         print(result, "Failed")
