customers = int(input())
sum1 = 0
items = 0
all_sums = 0
for _ in range(customers):
    while True:
        data = input()
        if data == "Finish":
            break
        items += 1
        if data == "basket":
            sum1 += 1.5
        elif data == "wreath":
            sum1 += 3.8
        elif data == "chocolate bunny":
            sum1 += 7
    if items % 2 == 0:
        sum1 *= 0.8
    print(f"You purchased {items} items for {sum1:.2f} leva.")
    all_sums += sum1
    sum1 = 0
    items = 0
print(f"Average bill per client is: {all_sums/customers:.2f} leva.")



