x = int(input())
y = int(input())
z = int(input())
free_space = x*y*z

while free_space > 0:
    data = input()
    if data == "Done":
        print(f"{free_space} Cubic meters left.")
        break
    else:
        free_space -= int(data)
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
