# Петя има магазин за детски играчки.
# Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Вход
# От конзолата се четат 6 реда:
# 1.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
trip_price = float(input())
# 2.	Брой пъзели - цяло число в интервала [0… 1000]
puzzles = int(input())
# 3.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
talking_dolls = int(input())
# 4.	Брой плюшени мечета - цяло число в интервала [0 … 1000]
teddy_bears = int(input())
# 5.	Брой миньони - цяло число в интервала [0 … 1000]
minions = int(input())
# 6.	Брой камиончета - цяло число в интервала [0 … 1000]
trucks = int(input())
# Изход
toys_count = puzzles+talking_dolls+teddy_bears+minions+trucks
total_money = puzzles*puzzle_price + \
    talking_doll_price * talking_dolls + \
    teddy_bears * teddy_bear_price + \
    minion_price *minions + \
    trucks * truck_price
if toys_count >= 50 :
    total_money = total_money * 0.75
total_money = total_money * 0.9
if total_money >= trip_price:
    print(f"Yes! {(total_money - trip_price):.2f} lv left.")
else:
    print(f"Not enough money! {(trip_price - total_money):.2f} lv needed.")


# На конзолата се отпечатва:
# •	Ако парите са достатъчни се отпечатва:
# o	"Yes! {оставащите пари} lv left."
# •	Ако парите НЕ са достатъчни се отпечатва:
# o	"Not enough money! {недостигащите пари} lv needed."
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.
