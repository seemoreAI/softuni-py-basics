flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_count = int(input())
yest = int(input())

sugar_price = flour_price*0.75
eggs_price = flour_price*1.1
yest_price = sugar_price*0.2

total_sum = flour_price * flour_kg + \
            sugar_price * sugar_kg + \
            eggs_price * eggs_count + \
            yest_price * yest

print(f"{total_sum:.2f}")






