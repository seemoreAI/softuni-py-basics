groups = int(input())
all_people = musala_people=monblan_people=kilimandjaro_people=k2_people=everest_people=0

for _ in range(groups):
    people = int(input())
    all_people += people
    if people <= 5:
        musala_people += people
    elif people > 5 and people <= 12:
        monblan_people += people
    elif people > 12 and people <= 25:
        kilimandjaro_people += people
    elif people > 25 and people <= 40:
        k2_people += people
    elif people > 40:
        everest_people += people

print(f'{musala_people/all_people*100:.2f}%')
print(f'{monblan_people/all_people*100:.2f}%')
print(f'{kilimandjaro_people/all_people*100:.2f}%')
print(f'{k2_people/all_people*100:.2f}%')
print(f'{everest_people/all_people*100:.2f}%')

