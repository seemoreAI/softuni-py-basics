btc = float(input())
juan = float(input())
comission = float(input())

sum = btc*1168 + (juan*0.15)*1.76
sum = sum / 1.95
sum = sum - sum*(comission/100)

print(f'{sum:.2f}')