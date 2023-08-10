
fruit = input()
variant = input()
count = int(input())

if fruit == "Watermelon":
    if variant == "small":
        price = 56 *2
    else:
        price = 28.70 * 5
elif fruit == "Mango":
    if variant == "small":
        price = 36.66 * 2
    else:
        price = 19.60 * 5
elif fruit == "Pineapple":
    if variant == "small":
        price = 42.10 * 2
    else:
        price = 24.80* 5
else:
    if variant == "small":
        price = 20 * 2
    else:
        price = 15.20* 5

suma = price * count


if 400 <= suma <= 1000:
    suma = suma * 0.85
elif suma > 1000:
    suma = suma * 0.5

print(f"{suma:.2f} lv.")

