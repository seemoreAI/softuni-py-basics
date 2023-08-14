# Дестинация	21-23 март	24-27 март	28-31 март
# Франция	30 лв.	35 лв.	40 лв.
# Италия	28 лв.	32 лв.	39 лв.
# Германия	32 лв.	37 лв.	43 лв.

destination = input()
dates = input()
nights = int(input())

if destination == "France":
    if dates == "21-23":
        price = 30
    elif dates == "24-27":
        price = 35
    elif dates == "28-31":
        price = 40
    else:
        price = 0

elif destination == "Italy":
    if dates == "21-23":
        price = 28
    elif dates == "24-27":
        price = 32
    elif dates == "28-31":
        price = 39
    else:
        price = 0
elif destination == "Germany":
    if dates == "21-23":
        price = 32
    elif dates == "24-27":
        price = 37
    elif dates == "28-31":
        price = 43
    else:
        price = 0
else:
    price = 0

total_price = price * nights

print(f"Easter trip to {destination} : {total_price:.2f} leva.")