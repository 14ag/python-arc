
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
