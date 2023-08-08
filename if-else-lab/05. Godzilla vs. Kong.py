# Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
# дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
budget = float(input())
decor_price = budget * 0.1
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
statists = int(input())
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
dress_price_for_one = float(input())
dress_price_total = dress_price_for_one * statists
if statists > 150:
    dress_price_total = dress_price_total * 0.9
# Изход
# На конзолата трябва да се отпечатат два реда:
# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.
total_price = dress_price_total + decor_price
if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price-budget:.2f} leva more." )
else:
    print("Action!")
    print(f"Wingard starts filming with {budget-total_price:.2f} leva left.")