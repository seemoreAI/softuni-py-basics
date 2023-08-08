hours = int(input())
minutes = int(input())

if minutes < 45:
    minutes = minutes + 15
elif hours < 23:
    hours += 1
    minutes = minutes + 15 - 60
else:
    hours = 0
    minutes = minutes + 15 - 60

print(f'{hours}:{minutes:02}')
