from math import floor
tournaments = int(input())
initial_point = int(input())
won_points = 0
won_tournaments = 0

for _ in range(tournaments):
    position = input()
    if position == "W":
        won_points += 2000
        won_tournaments += 1
    elif position == "F":
        won_points += 1200
    elif position == "SF":
        won_points += 720

print(f"Final points: {initial_point+won_points}")
print(f"Average points: {floor(won_points/tournaments)}")
print(f"{won_tournaments/tournaments*100:.2f}%")
