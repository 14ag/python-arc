 
 
You’ve officially unlocked **Set Theory** Using `set()` to handle duplicates is a professional-grade optimization. 
 
For your **14th hour**, we are going to look at **Array Manipulation and "In-Place" logic**. This is a common LeetCode theme: instead of just finding something, you have to "clean up" a list according to a specific rule. 
 
--- 
 
## LeetCode Style Challenge: "Move Zeroes" 
 
### Problem Statement: 
 
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements. 
 
**The Catch:** On LeetCode, "Easy" problems often ask you to do this **in-place**, but for your 14th hour, it's perfectly fine to create a new list and return it. 
 
### Constraints: 
 
* **Input:** `nums = [0, 1, 0, 3, 12]` 
* **Output:** `[1, 3, 12, 0, 0]` 
* **Requirement:** You cannot just "sort" the list (because sorting would put 1, 3, 12 in the wrong order if the input was `[0, 12, 3]`). 
 
--- 
 
### Key Concepts to Use: 
 
1. **Filtering:** Create a new list (let's call it `non_zeroes`) that only contains the numbers that are NOT zero. 
2. **Counting:** Keep track of how many zeroes you skipped. 
3. **Padding:** Use the `.append()` method or list multiplication (`[0] * count`) to add the zeroes back to the end of your `non_zeroes` list. 
 
### Example Test Cases: 
 
| Input | Expected Output | 
| --- | --- | 
| `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` | 
| `[0, 0, 1]` | `[1, 0, 0]` | 
| `[4, 5, 0, 1]` | `[4, 5, 1, 0]` | 
 
--- 
 
### Why this is a milestone: 
 
This problem introduces **Stable Filtering**. You are learning how to extract specific data while preserving the "history" (the order) of the rest of the data. In data processing, maintaining the sequence of events while removing "noise" (the zeroes) is a fundamental task. 
 
**Learn how to use "List Multiplication" to create a list of zeroes instantly** 
 
--- 
 
