video_price = 250
budget = float(input())
video_count = int(input())
video_total = video_count * video_price
cpu_price = video_total * 0.35
ram_price = video_total * 0.1
cpu_count = int(input())
ram_count = int(input())
ram_total = ram_count * ram_price
cpu_total = cpu_count * cpu_price
total_price = video_total + cpu_total + ram_total

if video_count > cpu_count:
    total_price = total_price * 0.85


if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
