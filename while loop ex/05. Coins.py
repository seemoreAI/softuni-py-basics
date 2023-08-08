money=float(input())
money = int(money * 100)
coins = 0
while money >= 200:
    money -= 200
    coins += 1
while money >= 100:
    money -= 100
    coins += 1
while money >= 50:
    money -= 50
    coins += 1
while money >= 20:
    money -= 20
    coins += 1
while money >= 10:
    coins += 1
    money -= 10
while money >= 5:
    coins += 1
    money -= 5
while money >= 2:
    coins += 1
    money -= 2
while money >= 1:
    coins += 1
    money -= 1
print(coins)


