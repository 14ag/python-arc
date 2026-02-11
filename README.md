You have reached a significant milestone After about 9 hours of Python, you are ready to tackle **Efficiency** and **Frequency Counting**. In the LeetCode world, this is a very common "Easy" level pattern.
This challenge moves away from just "cleaning" data and into **algorithmic thinking**.
---
## LeetCode Style Challenge: "Find the Lone Survivor"
### Problem Statement:
You are given a list of integers where every number appears **exactly twice**, except for one number which appears **only once**.
Your goal is to find that single, unique number.
### Constraints:
* **Input:** A list of integers (e.g., `nums = [2, 4, 6, 2, 4]`)
* **Output:** The integer that appears only once (e.g., `6`)
* **Goal:** Solve this using a **Dictionary** to count occurrences.
---
### Key Concepts to Use:
* **Frequency Mapping:** Create an empty dictionary. Loop through the list. If the number is already in the dictionary, increase its value. If not, add it with a value of 1.
* **Dictionary Iteration:** After the loop is finished, use `.items()` to loop through your dictionary and find the key that has a value of `1`.
### Example Test Cases:
| Input | Expected Output |
| --- | --- |
| `[1, 1, 2, 2, 3]` | `3` |
| `[10, 5, 10]` | `5` |
| `[9, 8, 7, 8, 9]` | `7` |
---
### Why this is a LeetCode classic:
This is a variation of the "Single Number" problem on LeetCode. It teaches you how to use a **Hash Map** (which is what a Python Dictionary is) to optimize searching. Searching a dictionary is much faster than searching a list over and over again.
---
**learn the "Counter" tool from the Python `collections` module, or build the frequency dictionary manually**
---
