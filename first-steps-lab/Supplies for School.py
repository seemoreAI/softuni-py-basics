pens = int(input())
markers = int(input())
liquid = int(input())
discount = int(input())

cena = pens * 5.80 + markers * 7.20 + liquid * 1.20
total = cena - cena * discount/100

print(total)
