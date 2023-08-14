from math import ceil
kozunaks = int(input())
total_flour = 0
total_sugar = 0
max_flour = 0
max_sugar = 0

for _ in range(kozunaks):
    current_sugar = float(input())
    current_flour = float(input())
    total_flour += current_flour
    total_sugar += current_sugar
    if current_flour > max_flour:
        max_flour = current_flour
    if current_sugar > max_sugar:
        max_sugar = current_sugar
print(f"Sugar: {ceil(total_sugar/950)}")
print(f"Flour: {ceil(total_flour/750)}")
print(f"Max used flour is {int(max_flour)} grams, max used sugar is {int(max_sugar)} grams.")
