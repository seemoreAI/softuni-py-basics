days = int(input())
money_total = 0
won_days = 0

for _ in range(days):
    games_played = 0
    money_today = 0
    wins = 0
    losses = 0

    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        games_played += 1
        if result == 'win':
            wins += 1
            money_today += 20
        else:
            losses += 1
    if losses < wins:
        money_today *= 1.1
        won_days += 1
    money_total += money_today

if days - won_days < won_days:
    money_total *= 1.2
    print(f"You won the tournament! Total raised money: {money_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_total:.2f}")
