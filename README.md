Hour 27. You’re handling sliding windows now, which means you're starting to care about the "cost" of your operations. Let's pivot to **In-Place Modification**.
This is a classic "LeetCode Easy" that is harder than it looks because it forces you to manage two different speeds of data processing simultaneously.
---
## LeetCode Style Challenge: "Remove Element"
### Problem Statement:
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**.
The order of the elements may be changed. You must do this by modifying the input array directly and returning the number of elements which are not equal to `val`.
### Constraints:
* **Input:** A list `nums` and a target `val`.
* **Output:** An integer  (the count of elements not equal to `val`).
* **The Reality:** You can't just return a new list. You have to shift the "valid" numbers to the front of the original list.
---
### Example Test Cases:
| Input `nums` | `val` | Expected Output (k) | Resulting `nums` (first k elements) |
| --- | --- | --- | --- |
| `[3, 2, 2, 3]` | `3` | `2` | `[2, 2, _, _]` |
| `[0, 1, 2, 2, 3, 0, 4, 2]` | `2` | `5` | `[0, 1, 3, 0, 4, _, _, _]` |
---
### Why this is a milestone:
This is the **Two-Pointer Write** pattern. You have one pointer looking for "good" data and another pointer keeping track of where that good data should be written.
But here's the thing: most beginners try to use `.remove()` or `.pop()` inside a loop. That's a disaster. Every time you remove an item, the list has to shift every other item over, turning your code into an  mess. Doing it "in-place" with pointers keeps it at .
---
### Your Objective:
1. Initialize a pointer (let's call it `k`) at 0.
2. Iterate through the array.
3. If the current element is NOT the `val` we want to remove, move that element to the position `nums[k]` and increment `k`.
4. Return `k`.
The reality is that memory is expensive. In embedded systems or massive databases, you don't get to just "make a copy" of your data. You have to fix it where it sits.
**Learn handle the pointer logic, or remember why `for i in range(len(nums))` is safer than `for x in nums` when you're modifying the index**
---
