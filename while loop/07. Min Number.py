min_number = float("inf")
data = input()
while data != 'Stop':
    data = int(data)
    if data < min_number:
        min_number = data
    data = input()
print(min_number)