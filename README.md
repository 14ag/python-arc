You have officially hit the **double-digit hours** mark By hour 11, you should be comfortable with list indexing, loops, and basic logic. Now it's time to introduce **Array Transformation**—a common pattern where you modify a list based on specific rules.
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
