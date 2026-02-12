 
 
You are absolutely crushing this After about 8 hours of Python, you’ve likely reached the point where you need to handle **Errors and Edge Cases**. In the real world, programs crash because users enter the wrong thing or data is missing. 
 
Your next milestone is learning how to make your code "bulletproof" using **Try/Except** blocks and **Type Checking**. 
 
--- 
 
## Challenge: The "Robust Calculator" 
 
### Problem Statement: 
 
You are building a division tool. Normally, division is easy, but two things can break a program: 
 
1. A user tries to divide by **Zero** (which is mathematically impossible). 
2. A user enters **Text** instead of a number. 
 
**Your task:** 
Write a function called `safe_divide` that takes two arguments, `a` and `b`. 
 
### The Requirements: 
 
* Try to divide `a` by `b` and **return** the result. 
* **If `b` is zero**, don't let the program crash `"Error: Cannot divide by zero."` 
* **If either input is not a number**, return the string: `"Error: Inputs must be numbers."` 
 
--- 
 
### Constraints: 
 
* **Input:** Two variables of any type. 
* **Tools:** Use a `try...except` block or `if` statements with `isinstance(a, (int, float))`. 
 
### Example Test Cases: 
 
```python 
print(safe_divide(10, 2))    # Expected: 5.0 
print(safe_divide(10, 0))    # Expected: "Error: Cannot divide by zero." 
print(safe_divide(10, "5"))  # Expected: "Error: Inputs must be numbers." 
 
``` 
--- 
 
### Why this is a milestone: 
 
This is the shift from "writing code that works" to **"writing professional code."** Professional software spends about 20% of its logic on the task and 80% on handling what might go wrong. 
 
--- 
 
**Learn the difference between a `ZeroDivisionError` and a `TypeError` so you can catch them specifically** 
 
--- 
