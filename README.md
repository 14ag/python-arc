You are flying through the fundamentals By the fifth hour, you’ve likely encountered **Dictionaries** (key-value pairs) and perhaps how to combine them with **Lists**. This is where you move from simple variables to managing actual "data."
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
