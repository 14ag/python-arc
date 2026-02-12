 
 
You are entering the "intermediate" beginner phase After about 7 hours of study, you are likely exploring **String Methods** and basic **Data Cleaning**. Real-world data is often "dirty" (extra spaces, mixed capitalization, or weird characters), and Python is the king of cleaning it up. 
 
--- 
 
## Challenge: The "Clean Tweet Hashtags" 
 
### Problem Statement: 
 
You are building a social media tool. You are given a list of messy hashtags entered by users. You need to "clean" them so they can be stored in a database. 
 
**Your task:** 
Write a program that takes a list of strings and transforms them into a clean format. 
 
### The Rules for "Cleaning": 
 
1. **Remove** any leading or trailing whitespace. 
2. Convert everything to **lowercase**. 
3. Ensure every string **starts with** a `#`. If it doesn't have one, add it. 
4. **Skip** any strings that are empty after cleaning. 
 
### Constraints: 
 
* **Input:** `tags = ["  Python ", "coding", "#DataScience", "  ", "sql  "]` 
* **Output:** A new list: `["#python", "#coding", "#datascience", "#sql"]` 
 
--- 
 
### Key Concepts to Use: 
 
* **`.strip()`**: Removes spaces from the start and end of a string. 
* **`.lower()`**: Converts the string to lowercase. 
* **`.startswith("#")`**: Checks if the first character is a hashtag. 
* **String Concatenation**: Using `"# " + tag` to add the symbol. 
 
--- 
 
### Example Test: 
 
```python 
raw_tags = ["  LEARN ", "#growth", " teaching", " "] 
# Your code should result in: 
# ["#learn", "#growth", "#teaching"] 
 
``` 
 
### Why this is a milestone: 
 
This is the first time you are **mutating** data (changing its form) and **filtering** data (removing the empty space) at the same time. This is the bread and butter of "Data Pre-processing." 
 
--- 
