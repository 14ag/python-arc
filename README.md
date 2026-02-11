For **Hour 21**, we're moving into **String Compression**. This is how zip files and image formats actually work under the hood.
---
## LeetCode Style Challenge: "Check if All Characters Have Equal Occurrences"
### Problem Statement:
Given a string `s`, return `True` if all characters that appear in `s` have the **same number of occurrences**, and `False` otherwise.
### Constraints:
* **Input:** A string (e.g., `"abacbc"`).
* **Output:** Boolean.
* **The Goal:** Don't use `.count()` inside a loop. Count everything once first.
### Example Test Cases:
| Input | Expected Output | Explanation |
| --- | --- | --- |
| `"abacbc"` | `True` | 'a', 'b', and 'c' all appear 2 times. |
| `"aaabb"` | `False` | 'a' appears 3 times, 'b' appears 2 times. |
| `"abcde"` | `True` | Everything appears exactly once. |
---
### Why this is a milestone:
You are learning to validate the **uniformity** of a dataset. In your last solution, you used the dictionary keys to find the "lucky" number. Here, you need to look at the dictionary **values**.
The reality is that once you have the counts, you don't care about the letters anymore. You just care if all the numbers in that dictionary are the same.
---
### Your Objective:
1. Loop through the string once to build a frequency dictionary (count the letters).
2. Get all the values from that dictionary (the counts).
3. Check if all those counts are equal.
**But here’s the thing:** There is a trick using a `set()` that can tell you if all values in a list are the same in one single line. Do you want to figure that out, or do you want to use a loop to compare the counts manually?
---
