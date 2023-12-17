# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0

extra_payment_start_month = 50
extra_payment_end_month = 102
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    if current_month >= 50 and current_month <= 102:
        principal = principal - extra_payment
    total_paid = total_paid + payment
    current_month += 1
    print(f"Current Month: {round(current_month, 2)}  ", end="")
    print(f"Total Paid: {round(total_paid, 2)}")

print("Total paid", round(total_paid, 2))