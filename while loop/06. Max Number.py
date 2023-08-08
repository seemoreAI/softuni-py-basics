max_number = float("-inf")
data = input()
while data != 'Stop':
    data = int(data)
    if data > max_number:
        max_number = data
    data = input()
print(max_number)
