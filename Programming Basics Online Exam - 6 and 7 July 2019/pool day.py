# От конзолата се четат 4 числа:
# 1.	Първи ред – брой на хората. Цяло число в интервала [1…100]
# 2.	Втори ред – такса вход. Реално число в интервала [0.00…50.00]
# 3.	Трети ред – цена един за шезлонг. Реално число в интервала [0.00…50.00]
# 4.	Четвърти ред – цена за един чадър. Реално число в интервала [0.00...50.00]
from math import ceil
humans = int(input())
tax_entry = float(input())
price_bed = float(input())
price_umbrella = float(input())
total_sum = 0

total_sum += tax_entry*humans
total_sum += price_bed*ceil(humans*0.75)
total_sum += price_umbrella*ceil(humans*0.5)

print(f"{total_sum:.2f} lv.")
