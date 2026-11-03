# 1 condition - if statement
# 1 condition, 2 outputs - if-else statement
# 2 conditions, 3 outputs - if-elif-else statement

# Topic 1: Conditional Statements
# Program 1: Smart Canteen Discount System
# Topic: if, elif, else, comparison operators, and logical thinking.
# Real-World Scenario
# Imagine a college canteen where students receive discounts based
# on their total bill.

# The canteen follows these rules:
# - If the bill is Rs. 3,000 or more, the student receives a
# 20% discount.
# - If the bill is Rs. 2,000 or more but less than Rs. 3,000,
# the student receives a 10% discount.
# - If the bill is Rs. 1,000 or more but less than Rs. 2,000,
# the student receives a 5% discount.
# - If the bill is less than Rs. 1,000, no discount is provided.
# - The program must display the original bill, discount amount,
# and final payable amount.

# Extra features:
# 1. A bill that is zero or negative is rejected, and the user is
#    asked to enter the amount again.
# 2. Students with a membership card get an extra 5% discount.
# 3. A "Congratulations! You saved..." message is shown when the
#    student receives a discount.

print("===== SMART CANTEEN =====")

while True:
    bill_amount = float(input("Enter your total bill amount (Rs.): "))
    if bill_amount <= 0:
        print("Invalid bill amount. Please enter an amount greater than zero.")
    else:
        break

if bill_amount >= 3000:
    discount_rate = 20
elif bill_amount >= 2000:
    discount_rate = 10
elif bill_amount >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount_amount = bill_amount * discount_rate / 100
amount_after_discount = bill_amount - discount_amount

membership = input("Do you have a membership card? (yes/no): ").strip().lower()

if membership == "yes":
    membership_discount = amount_after_discount * 5 / 100
else:
    membership_discount = 0

total_savings = discount_amount + membership_discount
final_amount = bill_amount - total_savings

print("\n===== BILL SUMMARY =====")
print(f"Original Bill: Rs. {bill_amount:.2f}")
print(f"Discount Rate: {discount_rate}%")
print(f"Discount Amount: Rs. {discount_amount:.2f}")
if membership == "yes":
    print(f"Membership Discount (5%): Rs. {membership_discount:.2f}")
print(f"Total Savings: Rs. {total_savings:.2f}")
print(f"Final Payable: Rs. {final_amount:.2f}")

if total_savings > 0:
    print(f"Congratulations! You saved Rs. {total_savings:.2f}")


# Practice Question:
# Student Challenge
# The program above already includes these features:
# 1. Invalid bill amount validation.
# 2. Extra 5% membership discount.
# 3. A savings message when a discount is applied.
# Teaching question: Why do we use elif instead of writing several
# independent if statements?
