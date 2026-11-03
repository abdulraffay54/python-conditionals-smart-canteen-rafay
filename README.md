# Python Conditional Statements — Smart Canteen Discount System

A beginner-friendly Python console program created during the Python lecture on **conditional statements**. It demonstrates how a program makes decisions using `if`, `elif`, and `else` in a realistic college-canteen scenario.

## Repository Name

`python-conditionals-smart-canteen`

## Discount Rules

| Bill Amount | Standard Discount |
|---|---:|
| Rs. 3,000 or more | 20% |
| Rs. 2,000 to below Rs. 3,000 | 10% |
| Rs. 1,000 to below Rs. 2,000 | 5% |
| Below Rs. 1,000 | 0% |

Members receive an **additional 5% discount** on the amount left after the standard discount.

## Program Features

The program starts with the basic canteen discount rules and adds three small features:

1. **Bill validation** — if the bill is zero or negative, a message is shown and the user is asked to enter the amount again. This uses a simple `while` loop.
2. **Membership discount** — if the student answers `yes` to having a membership card, an extra 5% discount is applied after the standard discount.
3. **Savings message** — when the student receives any discount, the program prints `Congratulations! You saved Rs. X`.

## Concepts Covered

- `if`: runs a block when a condition is true.
- `elif`: checks another condition when earlier conditions were false.
- `else`: handles the remaining case when no previous condition matched.
- Comparison operators such as `>=` and `<=`.
- Logical thinking about mutually exclusive conditions.
- Input using `input()` and numeric conversion using `float()`.
- A `while` loop that repeats until a valid bill amount is entered.
- Calculations with percentages.
- String formatting using f-strings and `:.2f`.
- A simple yes/no check with `if` and `else`.

## Discount Calculation

The membership discount is calculated **after** the standard discount.

For a Rs. 3,000 bill with a membership card:

1. Standard discount (20%): Rs. 600.00
2. Amount remaining: Rs. 2,400.00
3. Membership discount (5% of Rs. 2,400): Rs. 120.00
4. Total savings: Rs. 720.00
5. Final payable amount: Rs. 2,280.00

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python smart_canteen_discount.py
```

On some systems, use `python3` instead of `python`.

## Example Run

```text
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 3000
Do you have a membership card? (yes/no): yes

===== BILL SUMMARY =====
Original Bill: Rs. 3000.00
Discount Rate: 20%
Discount Amount: Rs. 600.00
Membership Discount (5%): Rs. 120.00
Total Savings: Rs. 720.00
Final Payable: Rs. 2280.00
Congratulations! You saved Rs. 720.00
```

## Invalid Bill Example

Zero and negative amounts are rejected, and the prompt repeats:

```text
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 0
Invalid bill amount. Please enter an amount greater than zero.
Enter your total bill amount (Rs.): -500
Invalid bill amount. Please enter an amount greater than zero.
Enter your total bill amount (Rs.): 1500
```

The program expects a number for the bill amount. Handling text input would need `try`/`except`, which is a later topic.

## UI/UX Notes

This is a **console-based** program, not a graphical web interface. Its basic user-experience choices are:

- A clear title and section separators.
- Direct prompts that tell the user what to enter.
- A friendly message for an invalid bill instead of stopping silently.
- Currency labels (`Rs.`) and two decimal places for money.
- A readable bill summary that shows the standard discount and membership discount separately.
- A positive message when the student saves money.

A future extension could add a graphical interface or web page, but that is outside the scope of this Python conditionals exercise.

## Teaching Note: Why `elif` Instead of Several `if` Statements?

`elif` is used because the discount tiers are **mutually exclusive**: a bill can only belong to one tier. When a condition matches, Python skips the rest of the chain, so the program cannot accidentally apply two standard discounts. Several independent `if` statements would run every check and would need extra care to avoid overlapping discounts.

## Practice Challenges

The original student challenges are now included. Further practice ideas:

1. Add a student category (e.g., student, staff, guest) with different discount rules.
2. Add a maximum discount limit.
3. Ask again if the membership answer is not `yes` or `no`.
4. Use a loop to calculate more than one bill without restarting the program.
5. Build an itemised order (several items and quantities) and calculate the bill from that list.
6. Print a receipt and save it to a text file.

## Suggested Git Commit

```text
Add validation, membership discount, and savings message to Smart Canteen
```

## Suggested Repository Description

Beginner Python lesson demonstrating if, elif, else, loops, and a real-world canteen discount calculator.
