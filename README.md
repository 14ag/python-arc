 
 
Hour 30. You've got XOR in your toolkit. Now we’re moving to **Coordinate Geometry** and **Monotonicity**. This sounds complex, but it's just checking if a sequence follows a consistent rule. 
 
--- 
 
## LeetCode Challenge: "Monotonic Array" 
 
### The Goal 
 
Determine if a given array is **monotonic**. 
 
An array is monotonic if it is either monotone increasing or monotone decreasing. 
 
* **Monotone increasing:** For all , . 
* **Monotone decreasing:** For all , . 
 
### The Task 
 
1. Take a list `nums`. 
2. Return `True` if the list only goes up (or stays flat) OR only goes down (or stays flat). 
3. Return `False` if it does both (e.g., it increases and then decreases). 
 
### Constraints 
 
* **Time Complexity:** . You should be able to decide the answer in one pass. 
* **Space Complexity:** . No extra lists or dictionaries. 
 
--- 
 
### Example Test Cases 
 
| Input `nums` | Expected Output | Explanation | 
| --- | --- | --- | 
| `[1, 2, 2, 3]` | `True` | It never decreases. | 
| `[6, 5, 4, 4]` | `True` | It never increases. | 
| `[1, 3, 2]` | `False` | It increases () then decreases (). | 
 
--- 
 
### Implementation Strategy 
 
You don't need to know if it's increasing or decreasing before you start. You can assume it's **both** at the beginning. As you walk through the array, if you see a pair of numbers that decreases, you know it's no longer "monotone increasing." If you see a pair that increases, you know it's no longer "monotone decreasing." 
 
By the end of the loop, if it hasn't failed *both* categories, it's monotonic. 
 
**try implementing this using two boolean flags, or compare the first and last elements first** 
 
--- 
 
