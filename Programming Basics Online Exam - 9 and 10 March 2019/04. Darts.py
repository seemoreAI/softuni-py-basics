total_points = 301
shots = 0
un_shots = 0
name = input()

while True:
    command = input()
    if command == "Retire":
        print(f"{name} retired after {un_shots} unsuccessful shots.")
        break

    points = int(input())

    if command == "Single":
        points = points
    elif command == "Double":
        points = 2*points
    elif command == "Triple":
        points = 3*points

    if points < total_points:
        total_points -= points
        shots += 1
    elif points == total_points:
        shots += 1
        print(f"{name} won the leg with {shots} shots.")
        break
    else:
        un_shots += 1
