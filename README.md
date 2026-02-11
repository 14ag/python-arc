You’re at **Hour 17**. You've handled strings and two-pointer logic. Now we're moving into **Math-Logic** and **Array Intersections**. This is a common pattern when you have two different sources of data and need to find the common ground between them.
---
## LeetCode Style Challenge: "Intersection of Two Arrays"
### Problem Statement:
Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**.
Each element in the result must be **unique** and you may return the result in **any order**.
### Constraints:
* **Input:** Two lists of integers.
* **Output:** A list containing only the numbers that appear in *both* input lists.
* **The Rule:** Even if a number appears five times in both lists, it should only appear **once** in your final result.
---
### Example Test Cases:
| Input `nums1` | Input `nums2` | Expected Output |
| --- | --- | --- |
| `[1, 2, 2, 1]` | `[2, 2]` | `[2]` |
| `[4, 9, 5]` | `[9, 4, 9, 8, 4]` | `[9, 4]` (or `[4, 9]`) |
| `[1, 2, 3]` | `[4, 5, 6]` | `[]` |
---
### Why this is a milestone:
This problem tests your ability to choose the most efficient tool for the job. You’ve worked with lists and sets. One of these is significantly faster for "checking existence" than the other. If you use a list for everything, your code will get sluggish as the data grows.
The reality is that "searching" is the most frequent thing a computer does. Doing it poorly costs time and money.
---
### Your Objective:
Find a way to compare these two lists. Don't worry about the "perfect" one-liner yet. Just focus on the logic of:
1. Identifying a common number.
2. Ensuring you don't add the same common number to your result twice.
**find a specific Set operator that makes this problem trivial**
**Learn "Reverse Iteration" in Python**
---
