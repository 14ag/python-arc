You are moving at an impressive pace By hour 12, you should be comfortable with list manipulation and logic. It’s time to tackle a **Search and Optimization** problem. This is a "LeetCode Easy" classic that introduces the concept of **Efficiency**.
---
## LeetCode Style Challenge: "The Target Sum" (Two Sum Lite)
### Problem Statement:
You are given a list of numbers and a **target** sum. You need to check if any two **distinct** numbers in that list add up exactly to the target.
Write a function `has_target_sum(nums, target)` that returns `True` if such a pair exists, and `False` otherwise.
### Constraints:
* **Input:** A list of integers `nums` and an integer `target`.
* **Output:** A Boolean (`True` or `False`).
* **Note:** You cannot use the same element twice (e.g., if the target is 4 and the list is `[2]`, the answer is `False`).
---
### Key Concepts to Use:
1. **Nested Loops:** You will likely need one loop inside another. The first loop picks a number, and the second loop checks all the *other* numbers to see if they add up to the target.
2. **Indexing:** Use `range(len(nums))` to make sure you aren't comparing a number to itself.
### Example Test Cases:
| Input | Target | Expected Output |
| --- | --- | --- |
| `[1, 4, 6, 10]` | `10` | `True` (4 + 6) |
| `[3, 2, 4]` | `6` | `True` (2 + 4) |
| `[1, 2, 3]` | `7` | `False` |
---
### Why this is a milestone:
This is your first encounter with **Time Complexity**.
* A "Nested Loop" solution (looping inside a loop) is called ****.
* As the list gets longer, this approach becomes very slow.
Once you solve this with two loops, the next "hour" of learning will teach you how to do it much faster using a **Set** or a **Dictionary**.
---
**Learn how to set up the nested `range()` loops so you don't accidentally count the same number twice**
---
