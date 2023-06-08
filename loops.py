# c=3
# while c:
#     print(c)
#     print("zero")
#     break
# print("done")


# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."

# x=0
# x=int(input("the"))
# s=777
# while x!=s:
#     print("Ha ha! You're stuck in my loop!")
#     x=int(input("the"))
# print("Well done, muggle! You are free now.")


# import time

# # Write a for loop that counts to five.
# for i in range(1,6):
#     # Body of the loop - print the loop iteration number and the word "Mississippi".
#     print(i,"Mississippi")
#     # Body of the loop - use: time.sleep(1)
#     time.sleep(1)
# # Write a print function with the final message.
# print("Ready or not, here I come!")


# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("the: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("The largest ", largest_number)
# else:
#     print("You haven't")





# ------------------------------------------------------
# The break statement is used to exit/terminate a loop.

# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

# # Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.

# x=""
# while x!="chupacabra":
#     x=input("the")#aws=use if to verify then break as a condition
#     continue
# print("You've successfully left the loop.")







#--------------------------------------------------------------------------
# Your task here is very special: you must design a vowel eater! Write a program that uses:
# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.

# x=input("the")
# x=x.upper()
# for i in x:
#     if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
#         continue
#     else:
#         print(i)
#------------------------------------------------------------------------------------------


blocks_input = int(input("Enter the number of blocks: "))
height = 0
layer_blocks = 1
while blocks >= layer_blocks:
    height += 1
    blocks -= layer_blocks
    layer_blocks += 1



        
