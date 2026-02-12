 
 
You are now at **Hour 15**, and you’ve mastered basic filtering and set-based optimization. Now, it's time to learn how to **search for a specific pattern** within a collection. This is a "LeetCode Easy" classic that introduces **Two-Pointer Logic**. 
 
--- 
 
## LeetCode Style Challenge: "Is Subsequence" 
 
### Problem Statement: 
 
Given two strings `s` and `t`, return `True` if `s` is a **subsequence** of `t`, or `False` otherwise. 
 
A **subsequence** of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not). 
 
### Constraints: 
 
* **Input:** Two strings, `s` and `t`. 
* **Output:** A Boolean (`True` or `False`). 
* **Goal:** Use a loop to "walk" through string `t` and see if you can find the characters of `s` in order. 
 
--- 
 
### Key Concepts to Use: 
 
1. **The Pointer Method:** Create a variable `i = 0` to track your position in string `s`. 
2. **The Main Loop:** Loop through every character in string `t`. 
3. **The Match:** If the current character in `t` matches `s[i]`, move your pointer `i` forward by 1. 
4. **The Finish Line:** If `i` ever becomes equal to the length of `s`, it means you found all the characters in order 
 
### Example Test Cases: 
 
| Input s | Input t | Expected Output | 
| --- | --- | --- | 
| `"abc"` | `"ahbgdc"` | `True` | 
| `"axc"` | `"ahbgdc"` | `False` (Missing 'x') | 
| `"ace"` | `"abcde"` | `True` | 
 
--- 
 
### Why this is a milestone: 
 
This is your first **Two-Pointer** problem. Instead of comparing two items in the *same* list, you are coordinating movement across *two different* strings. This logic is used in everything from DNA sequencing to search engine "auto-complete" features. 
 
--- 
 
**Learn how to handle the "IndexError" that might happen if you move your pointer past the end of string `s`, or are you ready to code** 
 
--- 
 
