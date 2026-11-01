"""
Topic: Python Conditional Statements
Program: Smart Canteen Discount System

Concepts covered:
- if, elif, and else
- Comparison operators
- Input conversion and validation
- Membership-based additional discount
- Arithmetic calculations
- Formatted output using f-strings

Scenario:
A college canteen gives discounts based on the student's bill:
- Rs. 3,000 or more: 20%
- Rs. 2,000 or more: 10%
- Rs. 1,000 or more: 5%
- Below Rs. 1,000: no standard discount

Members receive an additional 5% discount on the amount remaining
after the standard discount.
"""

print("=" * 32)
print("       SMART CANTEEN")
print("=" * 32)

# Step 1: Get and validate the bill amount.
try:
    bill_amount = float(input("Enter your total bill amount (Rs.): "))

    if bill_amount <= 0:
        print("Invalid bill! Please enter an amount greater than Rs. 0.")

    else:
        # Step 2: Select the standard discount using if / elif / else.
        if bill_amount >= 3000:
            discount_rate = 20
        elif bill_amount >= 2000:
            discount_rate = 10
        elif bill_amount >= 1000:
            discount_rate = 5
        else:
            discount_rate = 0

        standard_discount = bill_amount * discount_rate / 100
        amount_after_standard_discount = bill_amount - standard_discount

        # Step 3: Ask whether the student has a membership card.
        membership_answer = input(
            "Do you have a membership card? (yes/no): "
        ).strip().lower()

        if membership_answer == "yes":
            membership_discount = amount_after_standard_discount * 0.05
        else:
            membership_discount = 0

        # Step 4: Calculate total savings and final payable amount.
        total_discount = standard_discount + membership_discount
        final_amount = bill_amount - total_discount

        # Step 5: Display the bill summary.
        print("\n" + "=" * 32)
        print("         BILL SUMMARY")
        print("=" * 32)
        print(f"Original Bill:                 Rs. {bill_amount:.2f}")
        print(f"Standard Discount ({discount_rate}%):      Rs. {standard_discount:.2f}")
        print(f"Membership Discount:           Rs. {membership_discount:.2f}")
        print(f"Total Savings:                 Rs. {total_discount:.2f}")
        print(f"Final Payable Amount:          Rs. {final_amount:.2f}")

        if total_discount > 0:
            print(f"Congratulations! You saved Rs. {total_discount:.2f}.")
        else:
            print("No discount applied this time. Thank you for visiting!")

except ValueError:
    print("Invalid input! Please enter the bill amount as a number.")
