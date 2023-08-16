stage = input()
ticket_type = input()
ticket_quantity = int(input())
picture_with_tr = input()
price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = ticket_quantity * 55.5
    elif ticket_type == "Premium":
        price = ticket_quantity * 105.2
    elif ticket_type == "VIP":
        price = ticket_quantity * 118.9
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = ticket_quantity * 75.88
    elif ticket_type == "Premium":
        price = ticket_quantity * 125.22
    elif ticket_type == "VIP":
        price = ticket_quantity * 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        price = ticket_quantity * 110.10
    elif ticket_type == "Premium":
        price = ticket_quantity * 160.66
    elif ticket_type == "VIP":
        price = ticket_quantity * 400

if price > 4000:
    picture_with_tr = "N"
    price *= 0.75
elif price > 2500:
    price *= 0.9

if picture_with_tr == "Y":
    price = price + ticket_quantity*40

print(f"{price:.2f}")



