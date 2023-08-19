poroda = input()
gender = input()
months_life = 0

if poroda == "British Shorthair":
    if gender == "m":
        months_life = 13
    else:
        months_life = 14
elif poroda == "Siamese":
    if gender == "m":
        months_life = 15
    else:
        months_life = 16
elif poroda == "Persian":
    if gender == "m":
        months_life = 14
    else:
        months_life = 15
elif poroda == "Ragdoll":
    if gender == "m":
        months_life = 16
    else:
        months_life = 17
elif poroda == "American Shorthair":
    if gender == "m":
        months_life = 12
    else:
        months_life = 13
elif poroda == "Siberian":
    if gender == "m":
        months_life = 11
    else:
        months_life = 12
else:
    print(f"{poroda} is invalid cat!")
    exit()

print(f"{months_life*2} cat months")



