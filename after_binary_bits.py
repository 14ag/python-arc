import os
os.system('title lists')




# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prints the length of the existing list (Step 3).

y=int(input("the"))
x = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
x[2]=y
del x[-1]
print(len(x))
print(x)

