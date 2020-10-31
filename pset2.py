"""Each month, a credit card statement will come with the option for you to pay a minimum amount
of your charge, usually 2% of the balance due. However, the credit card company earns money
by charging interest on the balance that you don’t pay. So even if you pay credit card payments
on time, interest is still accruing on the outstanding balance. """


"""Problem 1
Write a program to calculate the credit card balance after one year if a person only pays the
minimum monthly payment required by the credit card company each month. """

balance = float(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))
payment_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))

total_amount_paid = 0
for i in range(1,13):
    print("Month", i)
    minimum_payment = balance * payment_rate
    print("Minimum monthly payment:", round(minimum_payment, 2))
    interest_payment = balance * (annual_interest_rate / 12)
    principle_paid = minimum_payment - interest_payment
    print("Principle paid:", round(principle_paid, 2))
    balance = balance - principle_paid
    print("Remaining balance:", round(balance, 2))
    total_amount_paid += minimum_payment

print("RESULT")
print("Total amount paid:", round(total_amount_paid, 2))
print("Remaining balance:", round(balance, 2))


###############################################################################

"""Problem 2
Now write a program that calculates the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. We will not be dealing with a minimum monthly
payment rate."""

balance = float(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))

monthly_interest_rate = annual_interest_rate / 12
monthly_payment = 0

while True:
    updated_balance = balance
    monthly_payment += 10
    month = 0
    for i in range(12):
        month += 1
        updated_balance = updated_balance * (1 + monthly_interest_rate) - monthly_payment
        if updated_balance <= 0:
            break
    if updated_balance <= 0:
        break


###############################################################################

"""Problem 3
Using Bisection Search to Make the Program Faster """

balance = float(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))

monthly_interest_rate = annual_interest_rate / 12
lower_bound = balance / 12
upper_bound = (balance * (1 + (annual_interest_rate / 12)) ** 12) / 12
epsilon = 0.1


while True:
    updated_balance = balance
    monthly_payment = (lower_bound + upper_bound) / 2
    month = 0
    for i in range(12):
        month += 1
        updated_balance = updated_balance * (1 + monthly_interest_rate) - monthly_payment
    if abs(updated_balance) - epsilon <= 0:
        break
    elif updated_balance > 0:
        lower_bound = monthly_payment
    else:
        upper_bound = monthly_payment 
    print(updated_balance)
    print(monthly_payment)

print("RESULT")
print("Monthly payment to pay off debt in 1 year:", round(monthly_payment, 2))
print("Number of months needed:", month)
print("Balance:", round(updated_balance, 2))