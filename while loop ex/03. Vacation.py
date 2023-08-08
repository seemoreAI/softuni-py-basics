money_needed = float(input())
money_saved = float(input())
days = 0
days_spent = 0

while money_saved < money_needed:
    action = input()
    money = float(input())
    days += 1
    if action == "save":
        money_saved += money
        days_spent = 0
    else:
        if money > money_saved:
            money_saved = 0
        else:
            money_saved = money_saved - money
        days_spent +=1
        if days_spent >= 5:
            print(f"You can't save the money.\n{days}")
            break
else:
    print(f"You saved the money for {days} days.")
