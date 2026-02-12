 
 
Hour 29. Let’s move to **Bit Manipulation** and **Parity**. This is a logic-heavy problem where you have to find a "needle in a haystack" based on frequency. 
 
--- 
 
## LeetCode Challenge: "Single Number" 
 
### The Goal 
 
Given a **non-empty** array of integers `nums`, every element appears **twice** except for one. Find that single one. 
 
### The Task 
 
1. Take a list `nums`. 
2. Identify the one integer that does not have a pair. 
3. Return that integer. 
 
### Constraints 
 
* **Time Complexity:** You must implement a solution with a linear  runtime. 
* **Space Complexity:** You must use only constant  extra space. (This means you **cannot** use a dictionary or a set to count occurrences). 
 
--- 
 
### Example Test Case 
 
| Input `nums` | Expected Output | Explanation | 
| --- | --- | --- | 
| `[2, 2, 1]` | `1` | 2 appears twice, 1 appears once. | 
| `[4, 1, 2, 1, 2]` | `4` | 1 and 2 both have pairs. 4 is alone. | 
| `[1]` | `1` | Only one element exists. | 
 
--- 
 
### Implementation Hint 
 
Since you aren't allowed to use extra memory (like a dictionary), you need a way to "cancel out" numbers that appear twice. 
 
There is a bitwise operator called **XOR** (`^` in Python). Here is how it behaves: 
 
*  (Any number XORed with itself becomes 0). 
*  (Any number XORed with 0 stays the same). 
* The order doesn't matter:  is the same as , which results in , which is just . 
 
If you XOR every number in the list together, the pairs will effectively delete each other, leaving only the single number behind. 
 
**Are you going to use the XOR trick, or do you want to try a different mathematical approach?** 
 
--- 
 
