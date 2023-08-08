# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

scr_type = input()
r = int(input())
c = int(input())

places = r * c
if scr_type == 'Premiere':
    price = places * 12
elif scr_type == 'Normal':
    price = places * 7.5
elif scr_type == 'Discount':
    price = places * 5
else:
    price = 0
print(f'{price:.2f}')
