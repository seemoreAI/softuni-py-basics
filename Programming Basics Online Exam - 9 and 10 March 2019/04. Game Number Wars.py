player1 = input()
player2 = input()
p1_points = 0
p2_points = 0

while True:
    command = input()
    if command == "End of game":
        print(f"{player1} has {p1_points} points")
        print(f"{player2} has {p2_points} points")
        break
    p1_card = int(command)
    p2_card = int(input())
    if p1_card > p2_card:
        p1_points += (p1_card - p2_card)
    elif p1_card < p2_card:
        p2_points += (p2_card - p1_card)
    else:
        print(f"Number wars!")
        if int(input()) > int(input()):
            print(f"{player1} is winner with {p1_points} points")
        else:
            print(f"{player2} is winner with {p2_points} points")
        break
