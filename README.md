 
 
You’ve hit **Hour 18**. You've mastered basic searching and unique sets. Now it’s time to deal with **Nested Data Structures**. In the real world, data isn't always a flat list of numbers; it’s often a list of lists (like a spreadsheet) or a matrix. 
 
--- 
 
## LeetCode Style Challenge: "Richest Customer Wealth" 
 
### Problem Statement: 
 
You are given an `m x n` integer grid called `accounts` where `accounts[i][j]` is the amount of money the -th customer has in the -th bank. Return the **wealth** of the richest customer. 
 
A customer's **wealth** is the sum of money they have in all their bank accounts. 
 
### Constraints: 
 
* **Input:** A list of lists (e.g., `[[1, 2, 3], [3, 2, 1]]`). 
* **Output:** A single integer representing the highest sum found. 
 
### Example Test Cases: 
 
| Input `accounts` | Expected Output | Explanation | 
| --- | --- | --- | 
| `[[1,2,3],[3,2,1]]` | `6` | Both customers have 6. | 
| `[[1,5],[7,3],[3,5]]` | `10` | The 2nd customer (7+3) is the richest. | 
| `[[2,8,7],[7,1,3],[1,9,5]]` | `17` | The 1st customer (2+8+7) is the richest. | 
 
--- 
 
### Why this is a milestone: 
 
This is your introduction to **2D Arrays**. You have to "loop within a loop"—the outer loop goes through each customer, and the inner loop (or a sum function) calculates their specific total. It forces you to keep track of a "global maximum" while doing local calculations. 
 
But here’s the thing: most beginners get confused about which index refers to the "row" and which refers to the "column." This challenge fixes that mental model. 
 
--- 
 
### Your Objective: 
 
1. Initialize a variable to keep track of the `max_wealth` (start it at 0). 
2. Iterate through each "customer" list in the main `accounts` list. 
3. Calculate the total for that specific customer. 
4. If their total is higher than your current `max_wealth`, update it. 
5. Return the final `max_wealth`. 
 
**Learn to use the `sum()` function to make the inner calculation easier, or manually loop through every single bank account** 
 
--- 
 
