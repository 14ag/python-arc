import os
os.system('cls')
os.system('prompt $G')
######################################################################
# Ask the user for the total amount of the bill (e.g., 50.00).
food_cost= float(input("what's the total ammount?: "))

# Ask the user what percentage they want to tip (e.g., 15).
tip=float(input("what percent would you like to tip?: "))
tip=(tip/100)*food_cost

# Ask the user how many people are splitting the bill.
friend_count= int(input("how many people did you eat with?: "))

# Calculate the total bill (bill + tip) and then divide it by the number of people.
individual_share=float( (food_cost+tip)/friend_count)
                   
# Print the final amount each person should pay.
print(individual_share)
