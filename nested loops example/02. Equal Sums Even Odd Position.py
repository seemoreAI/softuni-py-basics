n = int(input())
m = int(input())
sum_odd = sum_even = 0

for number in range(n, m+1):
    for j, digit in enumerate(str(number)):
        if j % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_odd == sum_even:
        print(number, end=' ')
    sum_odd = 0
    sum_even = 0

