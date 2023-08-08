# •	Първи ред - дни за престой - цяло число в интервала [0...365]
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
# •	Трети ред - оценка - "positive"  или "negative"
nights = int(input()) - 1
room_type = input()
feedback_type = input()
price = 0

if room_type == "room for one person":
    price = nights * 18

elif room_type == "apartment":
    price = nights * 25
    if nights < 10:
        price *= 0.7
    elif nights > 15:
        price *= 0.5
    else:
        price *= 0.65
elif room_type == "president apartment":
    price = nights * 35
    if nights < 10:
        price *= 0.9
    elif nights > 15:
        price *= 0.8
    else:
        price *= 0.85


if feedback_type == "positive":
    price *= 1.25
else:
    price *= 0.9

print(f'{price:.2f}')