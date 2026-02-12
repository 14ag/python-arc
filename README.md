 
 
Hour 34. You’re moving from finding pivots to **Cycle Detection** and **State Tracking**. This is a famous problem that looks like math but is actually about recognizing patterns in a sequence. 
 
--- 
 
## LeetCode Challenge: "Happy Number" 
 
### The Goal 
 
Determine if a number  is "happy." 
 
A **happy number** is a number defined by the following process: 
 
1. Starting with any positive integer, replace the number by the sum of the squares of its digits. 
2. Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1. 
3. Those numbers for which this process ends in 1 are happy. 
 
Return `True` if  is a happy number, and `False` if not. 
 
### The Task 
 
1. Write a helper to get the sum of squares of digits. (For `19`, it's ). 
2. Keep track of every result you get. 
3. If you hit `1`, return `True`. 
4. If you hit a number you have **seen before**, you are in a loop. Return `False`. 
 
### Constraints 
 
* **Memory:** Use a `set` to store the numbers you've already encountered. Checking a set is . 
 
--- 
 
### Example Test Case 
 
**Input:** `n = 19` 
 
1.  
2.  
3.  
4.  
**Output:** `True` 
 
**Input:** `n = 2` 
2, 4, 16, 37, 58, 89, 145, 42, 20, 4... (4 is repeated, so it loops forever). 
**Output:** `False` 
 
--- 
 
### Implementation Detail 
 
To split a number into digits without converting it to a string (which is slow), use the modulo operator `% 10` to get the last digit and integer division `// 10` to remove it. 
 
```python 
digit = n % 10 
n = n // 10 
 
``` 
 
**use a `while` loop with a `set` to catch the cycle, or try the "Floyd's Cycle-Finding" (Tortoise and Hare) approach to save memory** 
 
