total_sum = 0
data = input()
while data != 'NoMoreMoney':
    data = float(data)
    if data < 0:
        print("Invalid operation!")
        break
    total_sum += data
    print(f"Increase: {data:.2f}")
    data = input()
print(f"Total: {total_sum:.2f}")
