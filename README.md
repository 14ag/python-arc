 
 
Hour 33. You're moving from spatial logic to **Array Partitioning**. This is a logic puzzle that tests if you can find a "pivot point" in a stream of data. 
 
--- 
 
## LeetCode Challenge: "Find Pivot Index" 
 
### The Goal 
 
Given an array of integers `nums`, calculate the **pivot index** of this array. 
 
The **pivot index** is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index. 
 
### The Task 
 
1. Find the index where `sum(left_side) == sum(right_side)`. 
2. If the index is on the left edge (index 0), the left sum is 0. 
3. If the index is on the right edge, the right sum is 0. 
4. Return the **leftmost** pivot index. If no such index exists, return `-1`. 
 
### Constraints 
 
* **Efficiency:** . You must not use `sum()` inside your loop, as that would make the solution . 
* **Space:** . 
 
--- 
 
### Example Test Cases 
 
| Input `nums` | Expected Output | Explanation | 
| --- | --- | --- | 
| `[1, 7, 3, 6, 5, 6]` | `3` | Left sum = `1+7+3 = 11`. Right sum = `5+6 = 11`. | 
| `[1, 2, 3]` | `-1` | No index satisfies the condition. | 
| `[2, 1, -1]` | `0` | Left sum = `0`. Right sum = `1 + (-1) = 0`. | 
 
--- 
 
### Implementation Detail 
 
Don't overcomplicate it by slicing the list. 
 
1. Calculate the `total_sum` of the entire array once. 
2. Keep a running `left_sum` variable that starts at 0. 
3. As you iterate through the array, the `right_sum` is simply `total_sum - left_sum - nums[i]`. 
4. If `left_sum` equals that `right_sum`, you found your index. 
5. Update your `left_sum` by adding the current number before moving to the next iteration. 
 
The reality is that this is a classic "prefix sum" logic problem. It’s about using a known total to derive unknown parts without doing extra work. 
 
**learn how to handle the "leftmost" requirement** 
 
--- 
 
