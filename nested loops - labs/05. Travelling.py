while True:
    destination = input()
    if destination == "End":
        break
    sum_money = 0
    needed_money = float(input())
    while True:
        money = float(input())
        sum_money += money
        if sum_money >= needed_money:
            print(f"Going to {destination}!")
            break
