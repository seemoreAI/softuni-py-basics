win = lost = 0

while True:
    tournament = input()
    if tournament == "End of tournaments":
        break
    games = int(input())
    for i in range(1, games + 1):
        host_points = int(input())
        guest_points = int(input())
        if host_points > guest_points:
            print(f"Game {i} of tournament {tournament}: win with {host_points - guest_points} points.")
            win += 1
        else:
            print(f"Game {i} of tournament {tournament}: lost with {guest_points - host_points} points.")
            lost += 1
print(f"{win / (lost + win) * 100:.2f}% matches win")
print(f"{lost / (lost + win) * 100:.2f}% matches lost")
