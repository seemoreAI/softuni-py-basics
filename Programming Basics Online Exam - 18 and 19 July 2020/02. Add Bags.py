big_tax = float(input())
kilograms = float(input())
days = int(input())
quantity = int(input())

if kilograms < 10:
    big_tax *= 0.2
elif kilograms <= 20:
    big_tax *= 0.50

if days > 30:
    big_tax *= 1.1
elif days >= 7:
    big_tax *= 1.15
else:
    big_tax *= 1.4

price = big_tax * quantity


print(f" The total price of bags is: {price:.2f} lv. ")