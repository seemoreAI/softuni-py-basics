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

#following script is better, but only works in python after 3.10
#Judge will not be able to handle it, until update.

# match scr_type:
#     case 'Premiere':
#         price = places * 12
#     case 'Normal':
#         price = places * 7.5
#     case 'Discount':
#          price = places * 5
#     case _:
#          price = 0

print(f'{price:.2f}')
