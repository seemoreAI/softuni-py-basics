food = int(input())*1000

while True:
    data = input()
    if data == "Adopted":
        break
    else:
        food -= int(data)
if food >= 0:
    print(f"Food is enough! Leftovers: {food} grams.")
else:
    food = - food
    print(f"Food is not enough. You need {food} grams more.")
