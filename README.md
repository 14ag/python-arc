 
 
Excellent progress If you've just finished your second or third hour, you’ve likely encountered **Loops** (`for` or `while`) and **Lists**. 
 
This is where Python gets really powerful—handling "collections" of data instead of just one number or string at a time. 
 
--- 
 
## Challenge: The "Temperature Analyzer" 
 
### Problem Statement: 
 
You are given a list of daily high temperatures for a week. You need to write a program that analyzes this data to help a gardener decide if their plants are safe. 
 
**Your script should:** 
 
1. **Loop** through the list of temperatures. 
2. **Count** how many days were "Freezing" (below **32°F**). 
3. **Find** the highest temperature in the list. 
4. **Print** both the count of freezing days and the max temperature. 
 
### Constraints: 
 
* **Input:** A list of integers, e.g., `temps = [35, 28, 40, 31, 30, 45, 50]` 
* **Output:** A message like: *"There were 3 freezing days. The weekly high was 50."* 
 
--- 
 
### Key Concepts to Use: 
 
* **For Loops:** To look at each number in the list one by one. 
* **Counters:** A variable (like `count = 0`) that you increment inside the loop using `count = count + 1`. 
* **Comparison Logic:** Using `>` or `<` inside an `if` statement to compare the current temperature to your "max" variable. 
 
### Tips for Success: 
 
* To find the "Max" without using built-in shortcuts, create a variable called `highest` and set it to the first number in the list. Every time you find a number bigger than `highest`, update it 
* Python's indentation is critical—make sure your `if` statements are indented inside your `for` loop. 
 
--- 
 
