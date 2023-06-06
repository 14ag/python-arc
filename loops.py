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


largest_number = -99999999
counter = 0

while True:
    number = int(input("the: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest ", largest_number)
else:
    print("You haven't")
