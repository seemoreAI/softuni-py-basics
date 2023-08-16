won = 0
lost = 0
drawn = 0
for _ in range(3):
    game = input()
    if int(game[0]) > int(game[2]):
        won += 1
    elif int(game[0]) < int(game[2]):
        lost += 1
    else:
        drawn += 1
print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")


