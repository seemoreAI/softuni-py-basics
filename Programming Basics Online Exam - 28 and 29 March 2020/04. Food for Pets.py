days = int(input())
food = float(input())
cat_eat = 0
dog_eat = 0
biscuits = 0

for day in range(1, days+1):
    dog_eat_today = int(input())
    cat_eat_today = int(input())
    cat_eat += cat_eat_today
    dog_eat += dog_eat_today
    if day % 3 == 0:
        biscuits = biscuits + (cat_eat_today + dog_eat_today) * 0.1

total_eat = dog_eat + cat_eat

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eat/food*100:.2f}% of the food has been eaten.")
print(f"{dog_eat/total_eat*100:.2f}% eaten from the dog.")
print(f"{cat_eat/total_eat*100:.2f}% eaten from the cat.")




