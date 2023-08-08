flower_type = input()
quantity = int(input())
budget = int(input())

rose_price = 5
dalia_price = 3.80
tulip_price = 2.8
narcis_price = 3
gladiola_price = 2.5
total_price = 0
if flower_type == "Roses":
    total_price = quantity * rose_price
    if quantity > 80:
        total_price = total_price * 0.9
if flower_type == "Dahlias":
    total_price = quantity * dalia_price
    if quantity > 90:
        total_price = total_price * 0.85
if flower_type == "Tulips":
    total_price = quantity * tulip_price
    if quantity > 80:
        total_price = total_price * 0.85
if flower_type == "Narcissus":
    total_price = quantity * narcis_price
    if quantity < 120:
        total_price = total_price * 1.15
if flower_type == "Gladiolus":
    total_price = quantity * gladiola_price
    if quantity < 80:
        total_price = total_price * 1.2
if budget < total_price:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {quantity} {flower_type} and {budget - total_price:.2f} leva left.")

