minutes = int(input())
walkings = int(input())
calories = int(input())

burned = minutes*5*walkings

if calories / 2 <= burned:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned}.")
