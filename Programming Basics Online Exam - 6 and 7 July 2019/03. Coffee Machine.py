drink = input()             # •	Пстesso", "Cappuccino" или "Tea"
sugar = input()             # •	 с възможности "Without", "Normal" или "Extra"
quantity = int(input())     # •	Ттки - цяло число в интервала [1… 50]
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

total_price = quantity * price
# # Трябва да имате предвид следните отстъпки:
# # •	При избрана напитка без захар има 35% отстъпка.
if sugar == "Without":
    total_price *= .65
# # •	При избрана напитка "Espresso" и закупени поне 5 броя, има 25% отстъпка.
if drink == "Espresso" and quantity >= 5:
    total_price *= .75
# # •	При сума надвишава 15 лева, 20% отстъпка от крайната цена,
if total_price > 15:
    total_price *= .8

print(f"You bought {quantity} cups of {drink} for {total_price:.2f} lv.")
