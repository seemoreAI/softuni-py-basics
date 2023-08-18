wanted_profit = int(input())
profit_made = 0

while profit_made < wanted_profit:
    cocktail = input()
    if cocktail == "Party!":
        print(f"We need {wanted_profit - profit_made:.2f} leva more.")
        break
    price = len(cocktail)*int(input())
    if price % 2 != 0:
        price *= .75
    profit_made += price
else:
    print("Target acquired.")
print(f"Club income - {profit_made:.2f} leva.")

