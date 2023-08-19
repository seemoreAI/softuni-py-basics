from math import ceil
name = input()
budget = float(input())
beers = int(input())
chips = int(input())

beer_cost = 1.2 * beers
chips_price = 0.45 * beer_cost
chips_cost = ceil(chips_price * chips)
total_sum = chips_cost + beer_cost

if total_sum <= budget:
    print(f"{name} bought a snack and has {budget - total_sum:.2f} leva left.")
else:
    print(f"{name} needs {total_sum - budget:.2f} more leva!")



