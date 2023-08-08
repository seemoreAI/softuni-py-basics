month = input()
nights = int(input())
apartment_price = 0
studio_price = 0
apartment_total = 0
studio_total = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

apartment_total = apartment_price * nights
studio_total = studio_price * nights

if nights > 14 and month in ['May', 'October']:
    studio_total = studio_total * 0.7
if 7 < nights <= 14 and month in ['May', 'October']:
    studio_total = studio_total * 0.95
if nights > 14 and month in ['June', 'September']:
    studio_total = studio_total * 0.8
if nights > 14:
    apartment_total = apartment_total * 0.9

print(f'Apartment: {apartment_total:.2f} lv.')
print(f'Studio: {studio_total:.2f} lv.')


