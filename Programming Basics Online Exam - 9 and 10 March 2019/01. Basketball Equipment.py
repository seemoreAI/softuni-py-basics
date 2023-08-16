tax = int(input())

snikers = tax - tax * 0.40
ekip = snikers - snikers * 0.2
ball = ekip / 4
accesoars = ball / 5

print(f"{snikers + tax + accesoars + ekip + ball:.2f}")
