 
 
Hour 19. You’re handling 2D grids now. That's a huge jump. Most people get stuck there because they can't visualize the "list within a list." Since you've got that down, it’s time to tackle **Array Parity**. 
 
This is a favorite for interviewers because it tests if you can reorder data based on a specific property—in this case, whether a number is even or odd. 
 
--- 
 
## LeetCode Style Challenge: "Sort Array By Parity" 
 
### Problem Statement: 
 
Given an integer array `nums`, move all the **even integers** to the beginning of the array followed by all the **odd integers**. 
 
You can return the result in **any order** as long as the evens come before the odds. 
 
### Constraints: 
 
* **Input:** A list of integers (e.g., `[3, 1, 2, 4]`). 
* **Output:** A list where evens are first (e.g., `[2, 4, 3, 1]`). 
* **The Goal:** Don't just sort the list numerically. Use logic to separate them. 
 
--- 
 
### Example Test Cases: 
 
| Input | Possible Expected Output | 
| --- | --- | 
| `[3, 1, 2, 4]` | `[2, 4, 3, 1]` or `[4, 2, 1, 3]` | 
| `[0]` | `[0]` | 
| `[1, 2, 3, 4, 5, 6]` | `[2, 4, 6, 1, 3, 5]` | 
 
--- 
 
### Why this is a milestone: 
 
This is about **partitioning**. You’re learning how to split a dataset into two "buckets" and then stitch them back together. In data engineering, this is exactly how you'd separate valid records from corrupted ones or high-priority tasks from low-priority ones. 
 
The reality is that you don't always need a complex algorithm; sometimes you just need two empty lists and a way to join them at the end. 
 
--- 
 
### Your Objective: 
 
1. Create two separate empty lists: one for even numbers and one for odd. 
2. Loop through the input `nums`. 
3. Use the modulo operator (`%`) to check if a number is even. 
4. Put it in the right bucket. 
5. Combine the buckets and return the result. 
 
**Do this in a single line using List Comprehensions, or stick with the two-list approach** 
 
--- 
 
