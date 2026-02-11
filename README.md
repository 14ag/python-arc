For your **13th hour**, let's look at **Sets**. A Set in Python is like a dictionary without values; it allows you to check if an item exists almost instantly ().
---
## LeetCode Style Challenge: "Contains Duplicate"
### Problem Statement:
Given an integer array `nums`, return `True` if any value appears **at least twice** in the array, and return `False` if every element is distinct.
### Constraints:
* **Input:** A list of integers `nums`.
* **Goal:** Solve this **without** using `.count()`.
* **Hint:** Think about the properties of a `set()`. A set can only hold unique items. If you turn a list into a set, what happens to the length?
---
### Key Concepts to Use:
1. **The `set()` function:** `my_set = set(nums)` creates a collection of only the unique numbers from the list.
2. **Length Comparison:** If the number of items in the `set` is smaller than the number of items in the original `list`, it means there were duplicates.
### Example Test Cases:
| Input | Expected Output |
| --- | --- |
| `[1, 2, 3, 1]` | `True` |
| `[1, 2, 3, 4]` | `False` |
| `[1, 1, 1, 3, 3, 4]` | `True` |
---
### Why this is a milestone:
This is the "aha
---
**try writing this using the `len()` comparison trick, try a "one-by-one" approach where you add numbers to a set as you loop**
---
