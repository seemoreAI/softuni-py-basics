Best_payer = ""
Best_player_goals = 0
while True:
    player = input()
    if player == "END":
        break
    goals = int(input())
    if goals > Best_player_goals:
        Best_player_goals = goals
        Best_payer = player
    if goals >= 10:
        break

print(f"{Best_payer} is the best player!")

if Best_player_goals >= 3:
    print(f"He has scored {Best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {Best_player_goals} goals.")
