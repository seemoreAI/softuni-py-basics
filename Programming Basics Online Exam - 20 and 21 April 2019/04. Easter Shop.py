eggs_quantity = int(input())
selled_eggs = 0
while eggs_quantity >= 0:
    command = input()
    if command == "Close":
        print("Store is closed!")
        print(f"{selled_eggs} eggs sold.")
        break
    new_quantity = int(input())
    if command == "Buy":
        if new_quantity <= eggs_quantity:
            eggs_quantity -= new_quantity
            selled_eggs += new_quantity
        else:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs_quantity}.")
            break
    elif command == "Fill":
        eggs_quantity += new_quantity



