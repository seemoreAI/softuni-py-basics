x = int(input())
y = int(input())
total_pieces = x * y

while total_pieces > 0:
    data = input()
    if data == "STOP":
        print(f"{total_pieces} pieces are left.")
        break
    else:
        pieces = int(data)
        total_pieces -= pieces
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")



