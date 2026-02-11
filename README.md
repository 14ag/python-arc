Hour 20. You've been splitting lists and managing 2D grids. Now it's time to tackle **Relative Mapping**. This is a step up from basic counting because you have to use one set of data to "translate" or "rank" another.
On LeetCode, this falls under **Hashing and Sorting**.
---
## LeetCode Style Challenge: "Find Lucky Integer"
### Problem Statement:
A **lucky integer** is an integer that has a frequency in the array equal to its value.
Given an array of integers `arr`, return the **largest** lucky integer in the array. If there is no lucky integer, return `-1`.
### Example Test Cases:
| Input | Expected Output | Explanation |
| --- | --- | --- |
| `[2, 2, 3, 4]` | `2` | 2 appears 2 times. 3 appears 1 time (not lucky). |
| `[1, 2, 2, 3, 3, 3]` | `3` | 1, 2, and 3 are all lucky. 3 is the largest. |
| `[2, 2, 2, 3, 3]` | `-1` | 2 appears 3 times, 3 appears 2 times. None are lucky. |
---
### Why this is a milestone:
This is your first "Double Verification" problem. You aren't just checking if a number exists; you're checking if its **identity** matches its **behavior** (frequency).
It forces you to combine two things you've learned:
1. **Frequency Counting:** Using a dictionary to count how many times each number appears.
2. **Filtering & Comparison:** Looking through that dictionary to find the keys that match their values, then picking the biggest one.
---
### Your Objective:
1. Build a dictionary to store the counts of each number in `arr`.
2. Initialize a variable `largest_lucky = -1`.
3. Loop through the dictionary's "key-value" pairs.
4. Check if the `key` is equal to the `value`.
5. If it is, and it's bigger than your current `largest_lucky`, update your variable.
The reality is that "luck" here is just a data match. But the logic—comparing a key to its own frequency—is used constantly in fraud detection and pattern recognition.
**Learn how to use `max()` to find the largest lucky number more efficiently**
---
