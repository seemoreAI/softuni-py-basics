groups = int(input())
total_people = 0
group_1 = group_2 = group_3 = group_4 = group_5 = 0

for _ in range(groups):
    people = int(input())
    total_people += people
    if people < 6:
        group_1 += people
    elif people < 13:
        group_2 += people
    elif people < 26:
        group_3 += people
    elif people < 41:
        group_4 += people
    else:
        group_5 += people
total_people = group_1 + group_2 + group_3 + group_4 + group_5

print(f"{group_1/total_people*100:.2f}%")
print(f"{group_2/total_people*100:.2f}%")
print(f"{group_3/total_people*100:.2f}%")
print(f"{group_4/total_people*100:.2f}%")
print(f"{group_5/total_people*100:.2f}%")



