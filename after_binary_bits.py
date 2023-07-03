import os
os.system('title lists')




# # write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
# # write a line of code that removes the last element from the list (Step 2)
# # write a line of code that prints the length of the existing list (Step 3).

# y=int(input("the"))
# x = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# x[2]=y
# del x[-1]
# print(len(x))
# print(x)

# ______________________________________________________________________________



# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.



# # step 1
# beatles=[]
# print("Step 1:", beatles)

# # step 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)

# # step 3
# for i in range(2):
#     x=input("the")
#     beatles.append(x)
# print("Step 3:", beatles)

# # step 4
# del beatles[-2]
# del beatles[-1]
# print("Step 4:", beatles)

# # step 5
# beatles.insert(0,"Ringo Starr")
# print("Step 5:", beatles)


# # testing list legth
# print("The Fab", len(beatles))









# =-=-=-=-=-=--=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=--=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=--=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=--=-=-=-=-==-=-
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest)
# #second way of doing it using sort()
# print(sorted(my_list)[-1])






# =-=-=-=-=-=--=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=--=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=--=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=--=-=-=-=-==-=-

# Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.
# Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.
# Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.
# We've provided no test data, as that would be too easy. You can use our skeleton instead.



my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
print("The list with unique elements only:")
print(my_list)






