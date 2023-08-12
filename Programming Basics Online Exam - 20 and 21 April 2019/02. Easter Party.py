guests = int(input())
price_per_guest = float(input())
budget = float(input())

if guests > 20:
    price_per_guest = price_per_guest * 0.75
elif guests > 14:
    price_per_guest = price_per_guest * 0.80
elif guests > 9:
    price_per_guest = price_per_guest * 0.85

cake_price = budget * 0.1
total_price = guests * price_per_guest + cake_price

if total_price > budget:
    print(f'No party! {total_price - budget:.2f} leva needed.')
else:
    print(f'It is party time! {budget - total_price:.2f} leva left.')




