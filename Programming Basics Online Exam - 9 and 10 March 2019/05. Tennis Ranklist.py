tournaments = int(input())
initial_points = int(input())
wins = 0
points_from_tournaments = 0

for _ in range(tournaments):
    place = (input())
    if place == 'W':
        points_from_tournaments += 2000
        wins += 1
    elif place == 'F':
        points_from_tournaments += 1200
    elif place == 'SF':
        points_from_tournaments += 720

print(f"Final points: {initial_points+points_from_tournaments}")
print(f"Average points: {points_from_tournaments//tournaments}")
print(f"{wins/tournaments*100:.2f}%")


