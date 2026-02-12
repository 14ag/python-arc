 
 
The previous task was about removing elements. This task is about **merging** and **sorting** without using the built-in `.sort()` method. 
 
--- 
 
## LeetCode Challenge: "Merge Sorted Array" (In-Place) 
 
### The Goal 
 
You are given two integer arrays, `nums1` and `nums2`, each sorted in non-decreasing order. You are also given two integers, `m` and `n`, representing the number of actual elements in `nums1` and `nums2` respectively. 
 
Merge `nums2` into `nums1` as one sorted array. 
 
### The Task 
 
1. **Modify `nums1` in-place.** 2.  `nums1` has a total length of `m + n`. The first `m` elements are the data, and the last `n` elements are set to `0` (serving as empty placeholders for `nums2`). 
2. Combine them so that the final `nums1` is sorted. 
 
### Constraints 
 
* **Do not return a new list.** * **Do not use `nums1.sort()`.** 
* **Efficiency:** Aim for  time complexity. 
 
--- 
 
### Example Test Case 
 
**Input:** `nums1 = [1, 2, 3, 0, 0, 0]`, `m = 3` 
`nums2 = [2, 5, 6]`, `n = 3` 
 
**Output:** `nums1` becomes `[1, 2, 2, 3, 5, 6]` 
 
--- 
 
### Implementation Detail 
 
Since `nums1` has empty space at the **back**, it is often more efficient to compare the largest numbers from both lists and fill `nums1` from the **end** to the **front**. This prevents you from overwriting your own data as you move. 
 
1. Start a pointer at the end of the data in `nums1` (index ). 
2. Start a pointer at the end of `nums2` (index ). 
3. Start a "write" pointer at the very end of `nums1` (index ). 
4. Compare the values and place the larger one at the write pointer. 
 
--- 
 
