# AI Code Review Assignment (Python)

## Candidate
- Name: Bisrat Beriso
- Approximate time spent: 120 min

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Original code would crash if all orders were cancelled or the list was empty (division by zero).
-It used dictionary keys without quotes (order[status]), which would raise a NameError.
-It didn’t handle invalid or missing amount values, which could cause the program to crash.

### Edge cases & risks
- Input list is empty or all cancelled → should return 0.0.
- Orders list contains invalid items: None, non-dictionaries, empty dictionaries.
- Orders with "status" == "cancelled" must be ignored.
- Orders with invalid "amount" values (None, strings, lists) must be skipped.
- Input is not a list → function should return 0.0 safely.

### Code quality / design issues
- Original code lacked comments.
- Lacked proper error handling for invalid data.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added safe handling for empty lists and all-cancelled orders.
- Used quotes for dictionary keys (order["status"] and order["amount"]).
- Skip invalid items inside the list (None, non-dictionary items).
- Skip cancelled orders.
- Converted amount to float to handle numeric strings.
- Added try-except to skip invalid amounts.
- Added comments to explain each step.
- Added type hints to indicate input and output types.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would focus on:

**Normal orders** – e.g., a list of orders with amounts and status "completed".
- To confirm that the function correctly sums amounts and calculates the average.

**Cancelled orders** – e.g., orders with status "cancelled"
- The function should exclude cancelled orders from the average calculation.

**Empty order list** – []
- The function should return 0.0 and not crash.

**Orders with missing amount key** – e.g., {"status": "completed"}
- These orders should be skipped without raising errors.

**Orders with invalid amount values** – e.g., None, strings like "abc", or lists
- The function should safely skip these orders without crashing.

**All orders cancelled or invalid**
- The function should return 0.0 instead of raising a division by zero error.

**Mixed edge cases** – e.g., some cancelled, some invalid, some valid
- To ensure that only valid, non-cancelled orders are included in the average.

**Non-dictionary items** 
- skipped without crashing.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Did not mention how empty lists, missing fields, or invalid amounts are handled.
- Did not explain that it avoids crashing for edge cases.
-Did not mention handling of invalid items (None, non-dictionaries, missing keys).

### Rewritten explanation
- This function calculates the average value of all non-cancelled orders from a list of orders. It safely handles empty lists, cancelled orders, missing fields, and invalid amounts by skipping them. The function returns 0.0 if no valid orders exist.

## 4) Final Judgment
- Decision: Approve
- Justification: The corrected code correctly implements the intended behavior, handles edge cases safely, and is readable.
- Confidence & unknowns:High confidence in correctness.covers all realistic input scenarios.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Original code only checked for "@" in a string, which is too simplistic.
- Crashes if the list contains non-string entries like None or numbers.
- Counted emails with missing local or domain parts, e.g., "@example.com" or "user@".
- Counted emails with multiple @ symbols, e.g., "user@@example.com".

### Edge cases & risks
- Empty list → should return 0.
- Emails with leading/trailing spaces → not cleaned.
- Emails with invalid domains → "user@.com", "user@domain..com".
- Emails with invalid local part characters → spaces, special symbols not allowed in a normal email.
- If the input is not a list (e.g., None, string, or dictionary), the original code may crash or behave incorrectly.

### Code quality / design issues
- No comments explaining the function.
- Logic is overly simplistic and doesn’t handle realistic email formats.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added type checking to skip non-string entries.
- Trimmed spaces from emails.
- Ensured exactly one @ symbol per email.
- Checked that local and domain parts are non-empty.
- Validated local part: only letters, numbers, . _ + -.
- Validated domain part: must contain a dot, cannot start/end with dot, no consecutive dots.
- Added comments for clarity.
- Added a guard clause to return 0 when the input is not a list, preventing crashes and unexpected behavior.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

I would focus on the following areas:

**Normal valid emails** – e.g., "user@example.com", "user.name+tag@domain.co.uk"
- To confirm that standard emails are counted correctly.

**Empty input list** – []
- The function should return 0 and not crash.

**Non-string entries** – e.g., None, numbers, objects
- These should be safely ignored without causing errors.

**Malformed emails** – e.g., "user@", "@example.com", "user@@example.com"
- Ensures invalid emails are not counted.

**Emails with spaces** – e.g., " user@example.com "
- Leading/trailing spaces should be trimmed and valid emails counted.

**Domain checks** – e.g., "user@.com", "user@domain..com", "user@domain."
- Ensures that domains start and end properly, contain a dot, and do not have consecutive dots.

**Local part validation** – e.g., "user!@example.com", "user name@example.com"
- Ensures only allowed characters in the local part are counted.
**Input is not a list** (e.g., None, string, dictionary) -function should return 0 without raising an error.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Did not describe how “valid” emails are defined.
- Did not mention handling of non-string entries.
- Did not include checks for local/domain structure or consecutive dots.

### Rewritten explanation
- This function counts the number of valid email addresses in a list. An email is valid if it contains exactly one @, has non-empty local and domain parts, the domain contains a dot, does not start or end with a dot, and does not have consecutive dots. The local part may contain letters, numbers, dots, underscores, plus signs, and hyphens. Non-string entries and invalid emails are ignored. The function returns 0 if the list is empty or contains no valid emails.

## 4) Final Judgment
- Decision: Approve
- Justification: The corrected code handles edge cases, ignores invalid entries, validates realistic email structures, and includes clear comments
- Confidence & unknowns: High confidence that the function works correctly for common email formats and handles invalid input safely.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Original code counts all items in the list, including None, which can cause division by zero.
- Crashes if the input is not a list (e.g., None or a string).
- Crashes if the list contains non-numeric values (like "abc" or objects).

### Edge cases & risks
- Empty list → division by zero.
- All values are None → division by zero.
- Mixed types in the list → potential crash.
- Input is not a list → crash.

### Code quality / design issues
- No input validation.
- No comments.
- Variable names are not descriptive.
- count incorrectly includes invalid items instead of counting only valid numbers.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added input validation: return 0.0 if input is not a list.
- Skip invalid items: None and non-numeric values.
- Safely convert values to float with try/except.
- Count only valid numbers to avoid division by zero.
- Added docstring, comments, and type hints.
- Improved variable names for clarity (measurements, total_sum, valid_count, numeric_value).

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

**Normal numbers** → average should be correct.
**None values** → ignored.
**Invalid values** (strings, objects, lists) → skipped safely.
**Empty list** → returns 0.0.
**All invalid or None values** → returns 0.0.
**Mixed valid and invalid values** → only valid numbers are counted.
**Input is not a list** → safely returns 0.0.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Does not mention skipping invalid types (strings, objects, etc.).
- Does not mention empty list or all invalid values → division by zero risk.
- Does not mention input type validation.
- Variable names are not clear.

### Rewritten explanation
- This function calculates the average of valid numeric measurements in a list by ignoring None and any non-numeric values, while safely converting valid items to float. If the list is empty, contains no valid numbers, or is not a list, the function returns 0.0. Clear variable names and comments make the code easy to read, understand, and robust against invalid input.

## 4) Final Judgment
- Decision: Approve
- Justification: Corrected code safely handles invalid values, None, empty lists, and non-list inputs. It computes the average of valid numeric measurements without crashing or dividing by zero.
- Confidence & unknowns: High confidence, it covers all common and realistic cases.
 