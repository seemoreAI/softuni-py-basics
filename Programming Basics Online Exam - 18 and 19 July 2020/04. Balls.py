n = int(input())
Total_points = 0
Red_balls = Orange_balls = White_balls = 0
Yellow_balls = Other_colors = Black_balls = 0

for _ in range(n):
    col = input()
    if col == "red":
        Red_balls += 1
        Total_points += 5
    elif col == "white":
        White_balls += 1
        Total_points += 20
    elif col == "orange":
        Orange_balls += 1
        Total_points += 10
    elif col == "yellow":
        Yellow_balls += 1
        Total_points += 15
    elif col == "black":
        Black_balls += 1
        Total_points //= 2
    else:
        Other_colors += 1

print(f"Total points: {Total_points}")
print(f"Red balls: {Red_balls}")
print(f"Orange balls: {Orange_balls}")
print(f"Yellow balls: {Yellow_balls}")
print(f"White balls: {White_balls}")
print(f"Other colors picked: {Other_colors}")
print(f"Divides from black balls: {Black_balls}")



