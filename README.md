 
 
You are making incredible time By the sixth hour, you are likely moving beyond "how to write code" and into **"how to handle real-world data."** This usually involves **List Comprehensions** (a shorter way to write loops) or handling **Nested Data** (lists inside of lists). 
 
--- 
 
## Challenge: The "Classroom Grader" 
 
### Problem Statement: 
 
You have a list of students, where each student is represented by a **list** containing their name and their test score. Your job is to "filter" this data. 
 
**Your task:** 
Create a new list called `honors_students` that contains only the **names** of students who scored **90 or higher**. 
 
### Constraints: 
 
1. **Input:** A nested list like this: 
`students = [["Alice", 95], ["Bob", 78], ["Charlie", 92], ["David", 85]]` 
2. Use a **For Loop** (or a **List Comprehension** if you’ve learned it) to check each score. 
3. **Extract** only the name (the first element of the inner list). 
4. **Print** the final `honors_students` list. 
 
--- 
 
### Key Concepts to Use: 
 
* **Double Indexing:** If `student` is `["Alice", 95]`, then `student[0]` is the name and `student[1]` is the score. 
* **List Appending:** Using `.append()` to add a name to your new list. 
* **Filtering Logic:** An `if` statement to check if the score meets the requirement. 
 
### Example Output: 
 
Based on the input above, your output should be: 
`['Alice', 'Charlie']` 
 
--- 
 
### Why this is a milestone: 
 
In data science and web development, data almost always arrives in "nested" formats (like JSON). Learning how to "dig" into a list to pull out a specific piece of information is a superpower. 
 
--- 
