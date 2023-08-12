from math import ceil
kozunak_price = 4
egg_price = 0.45

guests = int(input())
budgets = int(input())

eggs = guests*2
kozunaks = ceil(guests/3)

total_cost = kozunak_price*kozunaks + egg_price*eggs

if budgets >= total_cost:
    print(f"Lyubo bought {kozunaks} Easter bread and {eggs} eggs.")
    print(f"He has {budgets - total_cost:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_cost - budgets:.2f} lv. more.")



