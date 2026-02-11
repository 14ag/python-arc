Hour 23. You’ve mastered frequency maps and dynamic thresholds. Now, let's look at **Data Transformation**. In many real-world scenarios, you aren't just looking for a number; you’re changing it based on its surroundings.
On LeetCode, this is a classic "Easy" that tests your ability to handle **Index Offsets**—looking at what comes before or after your current position.
---
## LeetCode Style Challenge: "Replace Elements with Greatest Element on Right Side"
### Problem Statement:
Given an array `arr`, replace every element in that array with the **greatest element** among the elements to its **right**, and replace the last element with `-1`.
### Example Test Case:
**Input:** `arr = [17, 18, 5, 4, 6, 1]`
**Output:** `[18, 6, 6, 6, 1, -1]`
**The Logic:**
* For `17`, the greatest element to its right is `18`.
* For `18`, the greatest element to its right is `6`.
* For `5`, the greatest element to its right is `6`.
* For `4`, the greatest element to its right is `6`.
* For `6`, the greatest element to its right is `1`.
* For `1`, there are no elements to the right, so it becomes `-1`.
---
### Why this is a milestone:
If you start from the beginning of the list, you have to look at the entire rest of the list for every single number. That's  and it's painfully slow.
But here’s the thing: if you start from the **end** of the list and walk **backward**, you only have to keep track of the "max seen so far." This turns a slow problem into a lightning-fast  solution.
---
### Your Objective:
1. Create a variable `max_so_far` and initialize it to `-1`.
2. Iterate through the array **backward** (from the last index to the first).
3. For each element:
* Save the current element in a temporary variable.
* Replace the current element with `max_so_far`.
* Update `max_so_far` to be whichever is bigger: the old `max_so_far` or the temporary variable you saved.
1. Return the modified array.
The reality is that "reverse thinking" is a common trick to optimize code. It prevents you from recalculating the same "max" over and over again.
**Learn how to use `range(len(arr) - 1, -1, -1)` to loop backward, or figure out the `reversed()` function**
---
