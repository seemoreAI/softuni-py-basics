free_volume = float(input())
i = 0
while free_volume > 0:
    data = input()
    if data == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    i += 1
    if i % 3 == 0:
        free_volume -= float(data)*1.1
    else:
        free_volume -= float(data)
else:
    i = i-1
    print("No more space!")
print(f"Statistic: {i} suitcases loaded.")
