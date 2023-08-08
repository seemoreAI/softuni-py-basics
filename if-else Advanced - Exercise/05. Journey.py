budget = float(input())
season = input() #•	Един от двата възможни сезона - "summer” или "winter”.
destination = "" # "Bulgaria", "Balkans" и "Europe"
type_place = "" # 'Camp' or 'Hotel'
spent_money = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == 'summer':
        type_place = 'Camp'
        spent_money = budget * 0.3
    elif season == 'winter':
        type_place = 'Hotel'
        spent_money = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == 'summer':
        type_place = 'Camp'
        spent_money = budget * 0.4
    elif season == 'winter':
        type_place = 'Hotel'
        spent_money = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    type_place = 'Hotel'
    spent_money = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_place} - {spent_money:.2f}")

