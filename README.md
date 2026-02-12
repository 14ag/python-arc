 
 
Hour 32. You’ve successfully flipped a matrix. Now we’re looking at **Boundary Logic** and **Adjacency**. This is a "LeetCode Easy" that requires you to handle edge cases—literally. 
 
--- 
 
## LeetCode Challenge: "Can Place Flowers" 
 
### The Goal 
 
You have a long flowerbed in which some of the plots are planted, and some are empty. However, flowers cannot be planted in **adjacent** plots. 
 
Given an integer array `flowerbed` containing `0`'s (empty) and `1`'s (not empty), and an integer `n`, return `True` if `n` new flowers can be planted in the `flowerbed` without violating the no-adjacent-flowers rule and `False` otherwise. 
 
### The Task 
 
1. Iterate through the `flowerbed`. 
2. A flower can be planted at index `i` only if: 
* `flowerbed[i]` is `0`. 
* The plot to the left (`i-1`) is empty or out of bounds. 
* The plot to the right (`i+1`) is empty or out of bounds. 
 
 
1. Every time you plant a flower, update the array and decrement `n`. 
2. If `n` hits zero, you’re done. 
 
### Constraints 
 
* **Efficiency:** . One pass. 
* **Modification:** You can modify the input array as you go to "reserve" the spots you’ve used. 
 
--- 
 
### Example Test Cases 
 
| Input `flowerbed` | `n` | Expected Output | Explanation | 
| --- | --- | --- | --- | 
| `[1, 0, 0, 0, 1]` | `1` | `True` | Can plant at index 2. | 
| `[1, 0, 0, 0, 1]` | `2` | `False` | Only one spot available. | 
| `[0, 0, 1]` | `1` | `True` | Can plant at index 0. | 
 
--- 
 
### Implementation Detail 
 
The main challenge is the **first** and **last** elements. 
 
* When `i == 0`, there is no `i-1`. 
* When `i == len(flowerbed) - 1`, there is no `i+1`. 
 
You need to write your `if` condition to handle these boundaries so you don't get an `IndexError`. Some people find it easier to "pad" the array with a `0` at the beginning and end, while others use explicit checks like `if i == 0 or flowerbed[i-1] == 0`. 
 
**Do you want to handle the boundary logic with `if/else` checks, or do you want to try the "padding" trick to simplify the loop?** 
 
--- 
 
