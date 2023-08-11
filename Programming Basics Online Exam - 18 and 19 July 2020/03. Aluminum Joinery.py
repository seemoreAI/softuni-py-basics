quantity = int(input())
if quantity < 10:
    print("Invalid order")
    exit()
type_joinery = input()
delivery = input()

if type_joinery == "90X130":
    price = 110
    if 30 < quantity <= 60:
        price *= .95
    elif quantity > 60:
        price *= .92
elif type_joinery == "100X150":
    price = 140
    if 40 < quantity <= 80:
        price *= .94
    elif quantity > 80:
        price *= .90
elif type_joinery == "130X180":
    price = 190
    if 20 < quantity <= 50:
        price *= .93
    elif quantity > 50:
        price *= .88
else:
    price = 250
    if 25 < quantity <= 50:
        price *= .91
    elif quantity > 50:
        price *= .86

total_price = price * quantity
if delivery == "With delivery":
    total_price += 60
if quantity > 99:
    total_price *= .96

print(f"{total_price:.2f} BGN")

