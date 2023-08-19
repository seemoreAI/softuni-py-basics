from math import ceil, floor

box_paint = int(input())
tapeti_rolls = int(input())
gloves_price = float(input())
chetka_price = float(input())

paint_cost = 21.5 * box_paint
tapeti_cost = 5.20 * tapeti_rolls
gloves = ceil(0.35 * tapeti_rolls)
gloves_cost = gloves * gloves_price
chetki = floor(0.48 * box_paint)
chetki_cost = chetki * chetka_price

total_cost = paint_cost + tapeti_cost + gloves_cost + chetki_cost

print(f"This delivery will cost {total_cost/15:.2f} lv.")

