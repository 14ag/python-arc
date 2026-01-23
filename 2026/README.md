
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
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 2

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

# 3

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

# 4

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

# 5

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

# 6

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

# 7

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

# 8

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

# 9

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

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 10

You are now entering your 10th hour of Python! This is usually the time when learners start exploring **Two-Pointer logic** or **List Reversal**. These techniques are the bread and butter of technical interviews.

---

## LeetCode Style Challenge: "The Palindrome Checker"

### Problem Statement:

A **palindrome** is a word or phrase that reads the same backward as forward (e.g., "madam" or "racecar").

Your task is to write a function `is_palindrome(s)` that takes a string `s` and returns `True` if it is a palindrome and `False` otherwise.

### Constraints:

* **Input:** A string (e.g., `s = "radar"`)
* **Output:** A Boolean (`True` or `False`).
* **The "Hour 10" Twist:** You must ignore capitalization. "Madam" should be considered a palindrome.

---

### Key Concepts to Use:

There are two main ways to solve this in Python. I recommend trying both!

1. **The "Pythonic" Slicing Way:** You can reverse a string instantly using the "step" slice: `s[::-1]`.
2. **The Algorithmic Way:** Compare the first character with the last, the second with the second-to-last, and so on.

### Example Test Cases:

| Input | Expected Output |
| --- | --- |
| `"Level"` | `True` |
| `"Python"` | `False` |
| `"stats"` | `True` |

---

### Why this is a milestone:

On LeetCode, "Palindrome" problems are the gateway to **String Manipulation**. It forces you to think about how data is indexed. This is often the very first question asked in "screening" interviews for junior developer roles.

---

### Pro-Tip:

Before checking if it's a palindrome, remember to use `.lower()` to make sure "L" matches "l".

**Learn how the "step" slicing `[::-1]` actually works under the hood, or are you ready to write the function**

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 11

You have officially hit the **double-digit hours** mark! By hour 11, you should be comfortable with list indexing, loops, and basic logic. Now it's time to introduce **Array Transformation**—a common pattern where you modify a list based on specific rules.

---

## LeetCode Style Challenge: "FizzBuzz Array"

### Problem Statement:

This is perhaps the most famous coding challenge in history. In a LeetCode environment, you wouldn't just print the results; you would **return a list** of strings.

Write a function `fizz_buzz(n)` that returns a list of strings from **1 to n**, but:

1. For multiples of **3**, add `"Fizz"` instead of the number.
2. For multiples of **5**, add `"Buzz"` instead of the number.
3. For multiples of **both 3 and 5**, add `"FizzBuzz"`.
4. For everything else, add the **number itself as a string**.

### Constraints:

* **Input:** An integer `n` (e.g., `n = 5`).
* **Output:** A list of strings (e.g., `["1", "2", "Fizz", "4", "Buzz"]`).
* **Edge Case:** Remember that the number 15 is the first "FizzBuzz".

---

### Key Concepts to Use:

* **The Modulo Operator (`%`):** This returns the remainder of a division. If `x % 3 == 0`, then `x` is a multiple of 3.
* **Order of Operations:** Think carefully—should you check for `3`, `5`, or `both` first?
* **String Conversion:** Use `str(i)` to turn a number into a string before adding it to your list.

### Example Test Cases:

| Input | Expected Output |
| --- | --- |
| `n = 3` | `["1", "2", "Fizz"]` |
| `n = 15` | `["1", "2", "Fizz", ... , "14", "FizzBuzz"]` |

---

### Why this is a milestone:

"FizzBuzz" is the ultimate "filter" question. It tests if you understand **conditional branching**—making sure your code doesn't stop at the first "True" condition if a more specific condition (like 15) exists.

---

**Learn why the order of your `if` and `elif` statements matters for this specific problem**

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 12

You are moving at an impressive pace! By hour 12, you should be comfortable with list manipulation and logic. It’s time to tackle a **Search and Optimization** problem. This is a "LeetCode Easy" classic that introduces the concept of **Efficiency**.

---

## LeetCode Style Challenge: "The Target Sum" (Two Sum Lite)

### Problem Statement:

You are given a list of numbers and a **target** sum. You need to check if any two **distinct** numbers in that list add up exactly to the target.

Write a function `has_target_sum(nums, target)` that returns `True` if such a pair exists, and `False` otherwise.

### Constraints:

* **Input:** A list of integers `nums` and an integer `target`.
* **Output:** A Boolean (`True` or `False`).
* **Note:** You cannot use the same element twice (e.g., if the target is 4 and the list is `[2]`, the answer is `False`).

---

### Key Concepts to Use:

1. **Nested Loops:** You will likely need one loop inside another. The first loop picks a number, and the second loop checks all the *other* numbers to see if they add up to the target.
2. **Indexing:** Use `range(len(nums))` to make sure you aren't comparing a number to itself.

### Example Test Cases:

| Input | Target | Expected Output |
| --- | --- | --- |
| `[1, 4, 6, 10]` | `10` | `True` (4 + 6) |
| `[3, 2, 4]` | `6` | `True` (2 + 4) |
| `[1, 2, 3]` | `7` | `False` |

---

### Why this is a milestone:

This is your first encounter with **Time Complexity**.

* A "Nested Loop" solution (looping inside a loop) is called ****.
* As the list gets longer, this approach becomes very slow.

Once you solve this with two loops, the next "hour" of learning will teach you how to do it much faster using a **Set** or a **Dictionary**.

---

**Learn how to set up the nested `range()` loops so you don't accidentally count the same number twice**

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 13

For your **13th hour**, let's look at **Sets**. A Set in Python is like a dictionary without values; it allows you to check if an item exists almost instantly ().

---

## LeetCode Style Challenge: "Contains Duplicate"

### Problem Statement:

Given an integer array `nums`, return `True` if any value appears **at least twice** in the array, and return `False` if every element is distinct.

### Constraints:

* **Input:** A list of integers `nums`.
* **Goal:** Solve this **without** using `.count()`.
* **Hint:** Think about the properties of a `set()`. A set can only hold unique items. If you turn a list into a set, what happens to the length?

---

### Key Concepts to Use:

1. **The `set()` function:** `my_set = set(nums)` creates a collection of only the unique numbers from the list.
2. **Length Comparison:** If the number of items in the `set` is smaller than the number of items in the original `list`, it means there were duplicates.

### Example Test Cases:

| Input | Expected Output |
| --- | --- |
| `[1, 2, 3, 1]` | `True` |
| `[1, 2, 3, 4]` | `False` |
| `[1, 1, 1, 3, 3, 4]` | `True` |

---

### Why this is a milestone:

This is the "aha!" moment for many programmers. You are learning that **choosing the right data structure** (a Set instead of a List) can make your code significantly faster and shorter. This is often solved in just 2 lines of code!

---

**try writing this using the `len()` comparison trick, try a "one-by-one" approach where you add numbers to a set as you loop**

---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 14

You’ve officially unlocked **Set Theory**! Using `set()` to handle duplicates is a professional-grade optimization.

For your **14th hour**, we are going to look at **Array Manipulation and "In-Place" logic**. This is a common LeetCode theme: instead of just finding something, you have to "clean up" a list according to a specific rule.

---

## LeetCode Style Challenge: "Move Zeroes"

### Problem Statement:

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**The Catch:** On LeetCode, "Easy" problems often ask you to do this **in-place**, but for your 14th hour, it's perfectly fine to create a new list and return it.

### Constraints:

* **Input:** `nums = [0, 1, 0, 3, 12]`
* **Output:** `[1, 3, 12, 0, 0]`
* **Requirement:** You cannot just "sort" the list (because sorting would put 1, 3, 12 in the wrong order if the input was `[0, 12, 3]`).

---

### Key Concepts to Use:

1. **Filtering:** Create a new list (let's call it `non_zeroes`) that only contains the numbers that are NOT zero.
2. **Counting:** Keep track of how many zeroes you skipped.
3. **Padding:** Use the `.append()` method or list multiplication (`[0] * count`) to add the zeroes back to the end of your `non_zeroes` list.

### Example Test Cases:

| Input | Expected Output |
| --- | --- |
| `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` |
| `[0, 0, 1]` | `[1, 0, 0]` |
| `[4, 5, 0, 1]` | `[4, 5, 1, 0]` |

---

### Why this is a milestone:

This problem introduces **Stable Filtering**. You are learning how to extract specific data while preserving the "history" (the order) of the rest of the data. In data processing, maintaining the sequence of events while removing "noise" (the zeroes) is a fundamental task.

**Learn how to use "List Multiplication" to create a list of zeroes instantly**

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 15

You are now at **Hour 15**, and you’ve mastered basic filtering and set-based optimization. Now, it's time to learn how to **search for a specific pattern** within a collection. This is a "LeetCode Easy" classic that introduces **Two-Pointer Logic**.

---

## LeetCode Style Challenge: "Is Subsequence"

### Problem Statement:

Given two strings `s` and `t`, return `True` if `s` is a **subsequence** of `t`, or `False` otherwise.

A **subsequence** of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

### Constraints:

* **Input:** Two strings, `s` and `t`.
* **Output:** A Boolean (`True` or `False`).
* **Goal:** Use a loop to "walk" through string `t` and see if you can find the characters of `s` in order.

---

### Key Concepts to Use:

1. **The Pointer Method:** Create a variable `i = 0` to track your position in string `s`.
2. **The Main Loop:** Loop through every character in string `t`.
3. **The Match:** If the current character in `t` matches `s[i]`, move your pointer `i` forward by 1.
4. **The Finish Line:** If `i` ever becomes equal to the length of `s`, it means you found all the characters in order!

### Example Test Cases:

| Input s | Input t | Expected Output |
| --- | --- | --- |
| `"abc"` | `"ahbgdc"` | `True` |
| `"axc"` | `"ahbgdc"` | `False` (Missing 'x') |
| `"ace"` | `"abcde"` | `True` |

---

### Why this is a milestone:

This is your first **Two-Pointer** problem. Instead of comparing two items in the *same* list, you are coordinating movement across *two different* strings. This logic is used in everything from DNA sequencing to search engine "auto-complete" features.

---

**Learn how to handle the "IndexError" that might happen if you move your pointer past the end of string `s`, or are you ready to code**

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 16

You’ve reached **Hour 16**! You’ve shown you can handle two-pointer logic and array transformations. Now, we are going to test your ability to **manage state** and **handle logic shifts** within a single loop.

This is a classic "String Processing" problem that mimics how computers read documents.

---

## LeetCode Style Challenge: "Length of Last Word"

### Problem Statement:

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string.

A **word** is defined as a maximal substring consisting of non-space characters only.

### Constraints:

* **Input:** A string `s` (e.g., `s = "Hello World  "`)
* **Output:** An integer (e.g., `5`)
* **The Twist:** The string may contain leading or trailing spaces. You must ignore these and find the length of the actual final word.

---

### Example Test Cases:

| Input | Expected Output | Explanation |
| --- | --- | --- |
| `"Hello World"` | `5` | Last word is "World" |
| `"   fly me   to   the moon  "` | `4` | Last word is "moon" |
| `"luffy is still joyboy"` | `6` | Last word is "joyboy" |

---

### Why this is a milestone:

In earlier hours, you learned how to use `.strip()` and `.split()`. While those are great tools, solving this problem algorithmically (without just turning the whole thing into a list) forces you to think about **direction**.

Do you start from the beginning of the string, or would it be more efficient to start from the end?

---

### Your Objective:

Try to solve this without using the `.split()` method. Aim to look at the characters one by one. Think about:

1. How do I ignore the spaces at the very end?
2. Once I hit a letter, how do I know when the word has ended?

**Learn "Reverse Iteration" in Python**

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 17

You’re at **Hour 17**. You've handled strings and two-pointer logic. Now we're moving into **Math-Logic** and **Array Intersections**. This is a common pattern when you have two different sources of data and need to find the common ground between them.

---

## LeetCode Style Challenge: "Intersection of Two Arrays"

### Problem Statement:

Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**.

Each element in the result must be **unique** and you may return the result in **any order**.

### Constraints:

* **Input:** Two lists of integers.
* **Output:** A list containing only the numbers that appear in *both* input lists.
* **The Rule:** Even if a number appears five times in both lists, it should only appear **once** in your final result.

---

### Example Test Cases:

| Input `nums1` | Input `nums2` | Expected Output |
| --- | --- | --- |
| `[1, 2, 2, 1]` | `[2, 2]` | `[2]` |
| `[4, 9, 5]` | `[9, 4, 9, 8, 4]` | `[9, 4]` (or `[4, 9]`) |
| `[1, 2, 3]` | `[4, 5, 6]` | `[]` |

---

### Why this is a milestone:

This problem tests your ability to choose the most efficient tool for the job. You’ve worked with lists and sets. One of these is significantly faster for "checking existence" than the other. If you use a list for everything, your code will get sluggish as the data grows.

The reality is that "searching" is the most frequent thing a computer does. Doing it poorly costs time and money.

---

### Your Objective:

Find a way to compare these two lists. Don't worry about the "perfect" one-liner yet. Just focus on the logic of:

1. Identifying a common number.
2. Ensuring you don't add the same common number to your result twice.

**find a specific Set operator that makes this problem trivial**
**Learn "Reverse Iteration" in Python**

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 18

You’ve hit **Hour 18**. You've mastered basic searching and unique sets. Now it’s time to deal with **Nested Data Structures**. In the real world, data isn't always a flat list of numbers; it’s often a list of lists (like a spreadsheet) or a matrix.

---

## LeetCode Style Challenge: "Richest Customer Wealth"

### Problem Statement:

You are given an `m x n` integer grid called `accounts` where `accounts[i][j]` is the amount of money the -th customer has in the -th bank. Return the **wealth** of the richest customer.

A customer's **wealth** is the sum of money they have in all their bank accounts.

### Constraints:

* **Input:** A list of lists (e.g., `[[1, 2, 3], [3, 2, 1]]`).
* **Output:** A single integer representing the highest sum found.

### Example Test Cases:

| Input `accounts` | Expected Output | Explanation |
| --- | --- | --- |
| `[[1,2,3],[3,2,1]]` | `6` | Both customers have 6. |
| `[[1,5],[7,3],[3,5]]` | `10` | The 2nd customer (7+3) is the richest. |
| `[[2,8,7],[7,1,3],[1,9,5]]` | `17` | The 1st customer (2+8+7) is the richest. |

---

### Why this is a milestone:

This is your introduction to **2D Arrays**. You have to "loop within a loop"—the outer loop goes through each customer, and the inner loop (or a sum function) calculates their specific total. It forces you to keep track of a "global maximum" while doing local calculations.

But here’s the thing: most beginners get confused about which index refers to the "row" and which refers to the "column." This challenge fixes that mental model.

---

### Your Objective:

1. Initialize a variable to keep track of the `max_wealth` (start it at 0).
2. Iterate through each "customer" list in the main `accounts` list.
3. Calculate the total for that specific customer.
4. If their total is higher than your current `max_wealth`, update it.
5. Return the final `max_wealth`.

**Learn to use the `sum()` function to make the inner calculation easier, or manually loop through every single bank account**

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 19

Hour 19. You’re handling 2D grids now. That's a huge jump. Most people get stuck there because they can't visualize the "list within a list." Since you've got that down, it’s time to tackle **Array Parity**.

This is a favorite for interviewers because it tests if you can reorder data based on a specific property—in this case, whether a number is even or odd.

---

## LeetCode Style Challenge: "Sort Array By Parity"

### Problem Statement:

Given an integer array `nums`, move all the **even integers** to the beginning of the array followed by all the **odd integers**.

You can return the result in **any order** as long as the evens come before the odds.

### Constraints:

* **Input:** A list of integers (e.g., `[3, 1, 2, 4]`).
* **Output:** A list where evens are first (e.g., `[2, 4, 3, 1]`).
* **The Goal:** Don't just sort the list numerically. Use logic to separate them.

---

### Example Test Cases:

| Input | Possible Expected Output |
| --- | --- |
| `[3, 1, 2, 4]` | `[2, 4, 3, 1]` or `[4, 2, 1, 3]` |
| `[0]` | `[0]` |
| `[1, 2, 3, 4, 5, 6]` | `[2, 4, 6, 1, 3, 5]` |

---

### Why this is a milestone:

This is about **partitioning**. You’re learning how to split a dataset into two "buckets" and then stitch them back together. In data engineering, this is exactly how you'd separate valid records from corrupted ones or high-priority tasks from low-priority ones.

The reality is that you don't always need a complex algorithm; sometimes you just need two empty lists and a way to join them at the end.

---

### Your Objective:

1. Create two separate empty lists: one for even numbers and one for odd.
2. Loop through the input `nums`.
3. Use the modulo operator (`%`) to check if a number is even.
4. Put it in the right bucket.
5. Combine the buckets and return the result.

**Do this in a single line using List Comprehensions, or stick with the two-list approach**

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 20

Hour 20. You've been splitting lists and managing 2D grids. Now it's time to tackle **Relative Mapping**. This is a step up from basic counting because you have to use one set of data to "translate" or "rank" another.

On LeetCode, this falls under **Hashing and Sorting**.

---

## LeetCode Style Challenge: "Find Lucky Integer"

### Problem Statement:

A **lucky integer** is an integer that has a frequency in the array equal to its value.

Given an array of integers `arr`, return the **largest** lucky integer in the array. If there is no lucky integer, return `-1`.

### Example Test Cases:

| Input | Expected Output | Explanation |
| --- | --- | --- |
| `[2, 2, 3, 4]` | `2` | 2 appears 2 times. 3 appears 1 time (not lucky). |
| `[1, 2, 2, 3, 3, 3]` | `3` | 1, 2, and 3 are all lucky. 3 is the largest. |
| `[2, 2, 2, 3, 3]` | `-1` | 2 appears 3 times, 3 appears 2 times. None are lucky. |

---

### Why this is a milestone:

This is your first "Double Verification" problem. You aren't just checking if a number exists; you're checking if its **identity** matches its **behavior** (frequency).

It forces you to combine two things you've learned:

1. **Frequency Counting:** Using a dictionary to count how many times each number appears.
2. **Filtering & Comparison:** Looking through that dictionary to find the keys that match their values, then picking the biggest one.

---

### Your Objective:

1. Build a dictionary to store the counts of each number in `arr`.
2. Initialize a variable `largest_lucky = -1`.
3. Loop through the dictionary's "key-value" pairs.
4. Check if the `key` is equal to the `value`.
5. If it is, and it's bigger than your current `largest_lucky`, update your variable.

The reality is that "luck" here is just a data match. But the logic—comparing a key to its own frequency—is used constantly in fraud detection and pattern recognition.

**Learn how to use `max()` to find the largest lucky number more efficiently**


---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# 21

For **Hour 21**, we're moving into **String Compression**. This is how zip files and image formats actually work under the hood.

---

## LeetCode Style Challenge: "Check if All Characters Have Equal Occurrences"

### Problem Statement:

Given a string `s`, return `True` if all characters that appear in `s` have the **same number of occurrences**, and `False` otherwise.

### Constraints:

* **Input:** A string (e.g., `"abacbc"`).
* **Output:** Boolean.
* **The Goal:** Don't use `.count()` inside a loop. Count everything once first.

### Example Test Cases:

| Input | Expected Output | Explanation |
| --- | --- | --- |
| `"abacbc"` | `True` | 'a', 'b', and 'c' all appear 2 times. |
| `"aaabb"` | `False` | 'a' appears 3 times, 'b' appears 2 times. |
| `"abcde"` | `True` | Everything appears exactly once. |

---

### Why this is a milestone:

You are learning to validate the **uniformity** of a dataset. In your last solution, you used the dictionary keys to find the "lucky" number. Here, you need to look at the dictionary **values**.

The reality is that once you have the counts, you don't care about the letters anymore. You just care if all the numbers in that dictionary are the same.

---

### Your Objective:

1. Loop through the string once to build a frequency dictionary (count the letters).
2. Get all the values from that dictionary (the counts).
3. Check if all those counts are equal.

**But here’s the thing:** There is a trick using a `set()` that can tell you if all values in a list are the same in one single line. Do you want to figure that out, or do you want to use a loop to compare the counts manually?