 
 
Hour 26. You’ve moved past simple counting and into the territory of structural relationships. Now we’re looking at **Stream Processing**. 
 
In this scenario, you aren't looking at the whole picture at once. You are looking at a "sliding" window of data. This is how video buffering or network packet analysis works. 
 
--- 
 
## LeetCode Style Challenge: "Maximum Average Subarray I" 
 
### Problem Statement: 
 
You are given an integer array `nums` and an integer `k`. 
 
Find a contiguous subarray (a slice of the list) whose length is equal to `k` that has the **maximum average value**, and return this value. 
 
### Constraints: 
 
* **Input:** A list of integers `nums` and a window size `k`. 
* **Output:** A float (the highest average found). 
* **The Trap:** If you recalculate the sum from scratch every time the window moves, your code will be too slow for large inputs. 
 
--- 
 
### Example Test Cases: 
 
| Input `nums` | `k` | Expected Output | Explanation | 
| --- | --- | --- | --- | 
| `[1, 12, -5, -6, 50, 3]` | `4` | `12.75` | The window `[12, -5, -6, 50]` has the max sum (51). 51/4 = 12.75. | 
| `[5]` | `1` | `5.0` | Only one possible window. | 
| `[0, 4, 0, 3, 2]` | `2` | `2.5` | The window `[3, 2]` has the max sum (5). 5/2 = 2.5. | 
 
--- 
 
### Why this is a milestone: 
 
This is the **Sliding Window** pattern. It’s a fundamental optimization technique. Instead of re-summing all `k` elements, you realize that when the window moves one step to the right, you just subtract the element that left the window and add the new one that entered. 
 
The reality is that efficiency here isn't about being "clever" with syntax; it's about reducing the number of mathematical operations the CPU has to perform. 
 
--- 
 
### Your Objective: 
 
Find the maximum sum of any `k` consecutive elements. Once you have the max sum, divide it by `k` at the very end to get the average. 
 
Think about how to update that sum as you iterate through the list without starting over from zero at every index. 
 
**Should I wait for your code, or do you want to see a test case with negative numbers to see if your logic holds up?** 
 
--- 
 
