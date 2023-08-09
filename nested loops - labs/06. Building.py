floors = int(input())
rooms = int(input())
letter = "L"

for i in range(floors,0,-1):
    for j in range(rooms):
        print(f"{letter}{i}{j} ", end="")
    print("")
    letter = "A" if i % 2 == 0 else "O"
