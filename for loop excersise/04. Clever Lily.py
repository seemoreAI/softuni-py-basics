age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
savings = 0

for i in range(1,age+1):
    if i % 2 == 0:
        savings += i*5 -1
    else:
        savings += toy_price

diff = f"{abs(savings-washing_machine_price):.2f}"

if savings >= washing_machine_price:
    print(f"Yes! {diff}")
else:
    print(f"No! {diff}")


