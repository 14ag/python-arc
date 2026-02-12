 
 
You are moving fast **Functions**. 
 
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
