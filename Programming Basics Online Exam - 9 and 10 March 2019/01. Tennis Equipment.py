from math import ceil,floor

rocket_price = float(input())
rocket_quantity = int(input())
sneakers_quantity = int(input())
sneakers_price = rocket_price / 6

total_price = (rocket_price*rocket_quantity + sneakers_price*sneakers_quantity)
total_price = total_price * 1.2

print(f"Price to be paid by Djokovic {floor(total_price/8)}")
print(f"Price to be paid by sponsors {ceil(total_price*7/8)}")

