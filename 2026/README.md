
#### formating guide
functions, classes => camelCase

files, variables=> snake_case


<br>
<br>
<br>

# 1
Welcome to the world of Python! After your first hour, you’ve likely learned about **variables**, **basic math**, **user input**, and perhaps how to **print** strings.

Here is a classic "First Hour" challenge that combines all those elements.

---

## The Challenge: The "Dinner Bill Splitter"

Write a program that helps a group of friends calculate how much each person owes at a restaurant, including a tip.

### Your Goal:

1. **Ask the user** for the total amount of the bill (e.g., 50.00).
2. **Ask the user** what percentage they want to tip (e.g., 15).
3. **Ask the user** how many people are splitting the bill.
4. **Calculate** the total bill (bill + tip) and then divide it by the number of people.
5. **Print** the final amount each person should pay.

### Things to remember:

* When you use `input()`, Python treats the data as a **string** (text). You will need to convert the bill and tip to a `float` (decimal number) and the number of people to an `int` (integer) to do math.
* **The Math:** To get the tip amount, you can use the formula:



---

### Example Output:

If the bill is **$100**, the tip is **18%**, and there are **2** people, your code should output something like:
`Each person should pay: $59.0`

---


Great job on the first challenge! If you’ve mastered variables and basic math, your next hour is likely spent learning about **If/Else statements** (logic) and perhaps your first **List** or **String manipulation**.

In "LeetCode" style, the problem focuses less on user interaction and more on a specific **logical goal** with defined inputs and outputs.

---

## LeetCode Style Challenge: "The Password Validator"

### Problem Statement:

You are building a login system. A valid password must meet two specific criteria:

1. It must be **at least 8 characters long**.
2. It must **not** contain any spaces.

Write a script that takes a string variable called `password` and determines if it is "Valid" or "Invalid."

### Constraints:

* **Input:** A string (e.g., `password = "Python123"`)
* **Output:** Print the word `"Valid"` if both conditions are met. Print `"Invalid"` otherwise.

---

### Key Concepts to Use:

* **`len()`**: This function counts how many characters are in a string (e.g., `len("Hi")` is 2).
* **`in` keyword**: You can check if a character exists in a string using `if " " in password:`.
* **`if / elif / else`**: To handle the logic flow.

### Example Test Cases:

| Input | Expected Output |
| --- | --- |
| `"PythonRocks"` | `Valid` |
| `"12345"` | `Invalid` (Too short) |
| `"Secret Code"` | `Invalid` (Contains a space) |

---



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 2

Excellent progress! If you've just finished your second or third hour, you’ve likely encountered **Loops** (`for` or `while`) and **Lists**.

This is where Python gets really powerful—handling "collections" of data instead of just one number or string at a time.

---

## Challenge: The "Temperature Analyzer"

### Problem Statement:

You are given a list of daily high temperatures for a week. You need to write a program that analyzes this data to help a gardener decide if their plants are safe.

**Your script should:**

1. **Loop** through the list of temperatures.
2. **Count** how many days were "Freezing" (below **32°F**).
3. **Find** the highest temperature in the list.
4. **Print** both the count of freezing days and the max temperature.

### Constraints:

* **Input:** A list of integers, e.g., `temps = [35, 28, 40, 31, 30, 45, 50]`
* **Output:** A message like: *"There were 3 freezing days. The weekly high was 50."*

---

### Key Concepts to Use:

* **For Loops:** To look at each number in the list one by one.
* **Counters:** A variable (like `count = 0`) that you increment inside the loop using `count = count + 1`.
* **Comparison Logic:** Using `>` or `<` inside an `if` statement to compare the current temperature to your "max" variable.

### Tips for Success:

* To find the "Max" without using built-in shortcuts, create a variable called `highest` and set it to the first number in the list. Every time you find a number bigger than `highest`, update it!
* Python's indentation is critical—make sure your `if` statements are indented inside your `for` loop.

---

<br>
<br>
<br>
<br>
<br>
<br>

# 3

You are moving fast! After about four hours of Python, you’ve likely reached one of the most important milestones in programming: **Functions**.

Functions allow you to wrap your code into reusable "tools" so you don't have to write the same logic over and over.

---

## Challenge: The "Currency Converter Function"

### Problem Statement:

Imagine you are building a travel app. You need a function that converts **USD** to **Euros**, but it also needs to subtract a small **transaction fee**.

**Your task:**
Create a function called `convert_currency` that:

1. Takes two **parameters**: `amount` (USD) and `rate` (the exchange rate).
2. Calculates the converted amount: .
3. Subtracts a **flat fee of ** from the final result.
4. **Returns** the final value.

### Constraints:

* If the result of the conversion is less than , the function should return `0` (because the fee covers the whole amount).
* You must use the `return` keyword.

---

### Example Test Cases:

```python
# Calling your function should look like this:
print(convert_currency(100, 0.92))  # Expected: 90.0 (100 * 0.92 - 2)
print(convert_currency(1, 0.92))    # Expected: 0    (Conversion is less than 2)

```

### Why this is the "Next Level":

* **Scope:** Variables created inside a function stay inside the function.
* **Return vs. Print:** This is a common point of confusion. `print()` shows a value to the human, but `return` gives the value back to the computer to use in other calculations.

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 4
You are flying through the fundamentals! By the fifth hour, you’ve likely encountered **Dictionaries** (key-value pairs) and perhaps how to combine them with **Lists**. This is where you move from simple variables to managing actual "data."

---

## Challenge: The "Inventory Manager"

### Problem Statement:

You are managing a small grocery store. You have a **Dictionary** where the **key** is the name of the fruit and the **value** is the quantity currently in stock.

**Your task:**
Write a program that takes an inventory dictionary and a "restock" list. It should update the quantities in the dictionary based on the list.

### Constraints:

1. Start with this dictionary: `inventory = {"apples": 5, "bananas": 12, "oranges": 0}`
2. You are given a list of items that just arrived: `shipment = ["apples", "oranges", "apples", "apples"]`
3. **Loop** through the `shipment` list.
4. For every item in the shipment, **increase** its count in the `inventory` dictionary by 1.
5. **Print** the final dictionary.

---

### Key Concepts to Use:

* **Dictionary Access:** How to get or update a value using its key (e.g., `inventory["apples"] += 1`).
* **Membership Checking:** Using `if item in inventory:` to make sure you don't try to update a fruit that isn't in your store.
* **Nested Logic:** Using a `for` loop to go through the list, and an `if` statement inside that loop to update the dictionary.

### Example Output:

After processing the shipment above, your `inventory` should look like this:
`{'apples': 8, 'bananas': 12, 'oranges': 1}`

---

### Why this is a milestone:

In the real world, data rarely comes in a single variable. Most apps (like Instagram or Amazon) work by looping through lists of dictionaries. Mastering this "nesting" is a huge step toward building real apps.

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 5
You are making incredible time! By the sixth hour, you are likely moving beyond "how to write code" and into **"how to handle real-world data."** This usually involves **List Comprehensions** (a shorter way to write loops) or handling **Nested Data** (lists inside of lists).

---

## Challenge: The "Classroom Grader"

### Problem Statement:

You have a list of students, where each student is represented by a **list** containing their name and their test score. Your job is to "filter" this data.

**Your task:**
Create a new list called `honors_students` that contains only the **names** of students who scored **90 or higher**.

### Constraints:

1. **Input:** A nested list like this:
`students = [["Alice", 95], ["Bob", 78], ["Charlie", 92], ["David", 85]]`
2. Use a **For Loop** (or a **List Comprehension** if you’ve learned it!) to check each score.
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
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 6

You are entering the "intermediate" beginner phase! After about 7 hours of study, you are likely exploring **String Methods** and basic **Data Cleaning**. Real-world data is often "dirty" (extra spaces, mixed capitalization, or weird characters), and Python is the king of cleaning it up.

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
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 6

You are absolutely crushing this! After about 8 hours of Python, you’ve likely reached the point where you need to handle **Errors and Edge Cases**. In the real world, programs crash because users enter the wrong thing or data is missing.

Your next milestone is learning how to make your code "bulletproof" using **Try/Except** blocks and **Type Checking**.

---

## Challenge: The "Robust Calculator"

### Problem Statement:

You are building a division tool. Normally, division is easy, but two things can break a program:

1. A user tries to divide by **Zero** (which is mathematically impossible).
2. A user enters **Text** instead of a number.

**Your task:**
Write a function called `safe_divide` that takes two arguments, `a` and `b`.

### The Requirements:

* Try to divide `a` by `b` and **return** the result.
* **If `b` is zero**, don't let the program crash! Instead, return the string: `"Error: Cannot divide by zero."`
* **If either input is not a number**, return the string: `"Error: Inputs must be numbers."`

---

### Constraints:

* **Input:** Two variables of any type.
* **Tools:** Use a `try...except` block or `if` statements with `isinstance(a, (int, float))`.

### Example Test Cases:

```python
print(safe_divide(10, 2))    # Expected: 5.0
print(safe_divide(10, 0))    # Expected: "Error: Cannot divide by zero."
print(safe_divide(10, "5"))  # Expected: "Error: Inputs must be numbers."

```

---

### Why this is a milestone:

This is the shift from "writing code that works" to **"writing professional code."** Professional software spends about 20% of its logic on the task and 80% on handling what might go wrong.

---

**Learn the difference between a `ZeroDivisionError` and a `TypeError` so you can catch them specifically**

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 7

You have reached a significant milestone! After about 9 hours of Python, you are ready to tackle **Efficiency** and **Frequency Counting**. In the LeetCode world, this is a very common "Easy" level pattern.

This challenge moves away from just "cleaning" data and into **algorithmic thinking**.

---

## LeetCode Style Challenge: "Find the Lone Survivor"

### Problem Statement:

You are given a list of integers where every number appears **exactly twice**, except for one number which appears **only once**.

Your goal is to find that single, unique number.

### Constraints:

* **Input:** A list of integers (e.g., `nums = [2, 4, 6, 2, 4]`)
* **Output:** The integer that appears only once (e.g., `6`)
* **Goal:** Solve this using a **Dictionary** to count occurrences.

---

### Key Concepts to Use:

* **Frequency Mapping:** Create an empty dictionary. Loop through the list. If the number is already in the dictionary, increase its value. If not, add it with a value of 1.
* **Dictionary Iteration:** After the loop is finished, use `.items()` to loop through your dictionary and find the key that has a value of `1`.

### Example Test Cases:

| Input | Expected Output |
| --- | --- |
| `[1, 1, 2, 2, 3]` | `3` |
| `[10, 5, 10]` | `5` |
| `[9, 8, 7, 8, 9]` | `7` |

---

### Why this is a LeetCode classic:

This is a variation of the "Single Number" problem on LeetCode. It teaches you how to use a **Hash Map** (which is what a Python Dictionary is) to optimize searching. Searching a dictionary is much faster than searching a list over and over again.

---

**learn the "Counter" tool from the Python `collections` module, or build the frequency dictionary manually**