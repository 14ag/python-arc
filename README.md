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
