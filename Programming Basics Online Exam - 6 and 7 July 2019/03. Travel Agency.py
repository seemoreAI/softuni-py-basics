town = input()
package = input()
vip = input()
days = int(input())

if days < 1:
    print("Days must be positive number!")
    exit()

vip_discount = 0
price = 0

if days > 7:
    days -= 1

if town in ("Bansko","Borovets"):
    if package == "noEquipment":
        price = 80
        vip_discount = 0.05
    elif package == "withEquipment":
        price = 100
        vip_discount = 0.1
    else:
        print("Invalid input!")
        exit()
elif town in ("Varna","Burgas"):
    if package == "noBreakfast":
        price = 100
        vip_discount = 0.07
    elif package == "withBreakfast":
        price = 130
        vip_discount = 0.12
    else:
        print("Invalid input!")
        exit()
else:
    print("Invalid input!")
    exit()

total_price = price * days
if vip == 'yes':
    total_price = total_price - total_price * vip_discount


print(f"The price is {total_price:.2f}lv! Have a nice time!")







