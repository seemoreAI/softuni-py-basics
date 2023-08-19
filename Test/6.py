locations = int(input())

for _ in range(locations):
    planned_gold = float(input())
    days = int(input())
    dug_gold = 0
    for _ in range(days):
        dug_gold += float(input())
    if dug_gold / days >= planned_gold:
        print(f"Good job! Average gold per day: {dug_gold / days:.2f}.")
    else:
        print(f"You need {planned_gold - dug_gold / days:.2f} gold.")
