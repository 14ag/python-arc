 
 
Hour 31. You've handled monotonic trends and bit manipulation. Now we’re moving into **Matrix Transformation**. This is a test of how you manipulate indices in a 2D coordinate system. 
 
--- 
 
## LeetCode Challenge: "Transpose Matrix" 
 
### The Goal 
 
Given a 2D integer array `matrix`, return the **transpose** of the matrix. 
 
The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices. 
 
### The Task 
 
1. Take a 2D list `matrix` where `matrix[r][c]` represents the element at row `r` and column `c`. 
2. Create a new matrix where the element at `result[c][r]` is the original `matrix[r][c]`. 
3. **Return the new matrix.** 
 
### Constraints 
 
* **Input size:** The matrix is not necessarily square (e.g., it could be ). 
* **Output:** If the input is $R \times C$, the , the output must be  $C \times R$. 
 
--- 
 
### Example Test Case 
 
**Input:** ```python 
matrix = [[1, 2, 3], 
[4, 5, 6]] 
 
``` 
**Output:** ```python 
[[1, 4],  
 [2, 5],  
 [3, 6]] 
 
``` 
 
--- 
 
### Implementation Detail 
 
Since the dimensions flip, you first need to determine the number of rows and columns in the original. 
 
* `rows = len(matrix)` 
* `cols = len(matrix[0])` 
 
You’ll need to initialize a new 2D grid with the dimensions swapped. In Python, you can create a "blank" grid of zeros like this: 
`result = [[0] * rows for _ in range(cols)]` 
 
Then, use a nested loop to map the old coordinates to the new ones. 
 
**Are you going to build the result matrix manually using loops, or do you want to try the Pythonic `zip(*matrix)` trick?** 
 
--- 
 
