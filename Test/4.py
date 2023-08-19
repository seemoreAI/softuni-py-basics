cat_quantity = int(input())
g1 = g2 = g3 = 0
all_food = 0

for _ in range(cat_quantity):
    kg_food = float(input())
    all_food += kg_food
    if 100 <= kg_food < 200:
        g1 += 1
    elif 200 <= kg_food < 300:
        g2 += 1
    elif 300 <= kg_food <= 400:
        g3 += 1
    else:
        print("Error")
        exit()

print(f"Group 1: {g1} cats.")
print(f"Group 2: {g2} cats.")
print(f"Group 3: {g3} cats.")
print(f"Price for food per day: {all_food/1000*12.45:.2f} lv.")



