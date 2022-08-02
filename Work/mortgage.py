# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months_paid = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108


while principal > 0:
    months_paid += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if months_paid >= extra_payment_start_month and months_paid <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
if principal < 0:
    print(f'Returning ${principal} to you')

print('Total paid', total_paid, 'over', months_paid, 'months')
