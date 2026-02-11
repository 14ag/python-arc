You’ve reached **Hour 16** You’ve shown you can handle two-pointer logic and array transformations. Now, we are going to test your ability to **manage state** and **handle logic shifts** within a single loop.
This is a classic "String Processing" problem that mimics how computers read documents.
---
## LeetCode Style Challenge: "Length of Last Word"
### Problem Statement:
Given a string `s` consisting of words and spaces, return the length of the **last** word in the string.
A **word** is defined as a maximal substring consisting of non-space characters only.
### Constraints:
* **Input:** A string `s` (e.g., `s = "Hello World  "`)
* **Output:** An integer (e.g., `5`)
* **The Twist:** The string may contain leading or trailing spaces. You must ignore these and find the length of the actual final word.
---
### Example Test Cases:
| Input | Expected Output | Explanation |
| --- | --- | --- |
| `"Hello World"` | `5` | Last word is "World" |
| `"   fly me   to   the moon  "` | `4` | Last word is "moon" |
| `"luffy is still joyboy"` | `6` | Last word is "joyboy" |
---
### Why this is a milestone:
In earlier hours, you learned how to use `.strip()` and `.split()`. While those are great tools, solving this problem algorithmically (without just turning the whole thing into a list) forces you to think about **direction**.
Do you start from the beginning of the string, or would it be more efficient to start from the end?
---
### Your Objective:
Try to solve this without using the `.split()` method. Aim to look at the characters one by one. Think about:
1. How do I ignore the spaces at the very end?
2. Once I hit a letter, how do I know when the word has ended?
**Learn "Reverse Iteration" in Python**
---
