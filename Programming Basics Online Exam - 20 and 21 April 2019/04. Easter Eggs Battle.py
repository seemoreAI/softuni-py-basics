first_payer_eggs = int(input())
second_payer_eggs = int(input())

while first_payer_eggs > 0 and second_payer_eggs > 0:
    winner = input()
    if winner == "End":
        print(f"Player one has {first_payer_eggs} eggs left.")
        print(f"Player two has {second_payer_eggs} eggs left.")
        break
    if winner == "one":
        second_payer_eggs -= 1
    elif winner == "two":
        first_payer_eggs -= 1

else:
    if first_payer_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_payer_eggs} eggs left.")
    else:
        print(f"Player two is out of eggs. Player one has {first_payer_eggs} eggs left.")


