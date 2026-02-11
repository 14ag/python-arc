Hour 25. You're deep enough into this that you don't need a map. You just need the problem.
This one is about **Pattern Matching**. It’s a step up from the Ransom Note because the relationship isn't just about "having enough letters"—it’s about the **structure** of the data.
---
## LeetCode Style Challenge: "Isomorphic Strings"
### Problem Statement:
Two strings `s` and `t` are **isomorphic** if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same replacement character, but a character may map to itself.
### Constraints:
* **Input:** Two strings, `s` and `t`.
* **Output:** Boolean (`True` or `False`).
* **Requirement:** The mapping must be consistent. If 'a' maps to 'x' once, it must always map to 'x'. And 'b' cannot also map to 'x'.
---
### Example Test Cases:
| Input `s` | Input `t` | Expected Output | Explanation |
| --- | --- | --- | --- |
| `"egg"` | `"add"` | `True` | 'e' -> 'a', 'g' -> 'd' |
| `"foo"` | `"bar"` | `False` | 'o' cannot map to both 'a' and 'r' |
| `"paper"` | `"title"` | `True` | Consistent 1-to-1 mapping |
| `"badc"` | `"baba"` | `False` | 'd' and 'c' both try to map to 'a' |
---
### Why this is a milestone:
This is your first encounter with **Bi-directional Mapping**. It’s not enough to know that "A becomes B." You also have to ensure that "B only comes from A."
The reality is that this is how basic encryption and substitution ciphers work. If your logic is leaky, the "code" breaks. You have to track relationships, not just counts.
---
### Your Objective:
Figure out how to maintain a record of which character "belongs" to which. If you hit a contradiction—where a character is already promised to something else—you've failed the isomorphism test.
---
