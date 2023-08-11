n = int(input())
m = int(input())

for number in range(n, m+1):
    sum_odd = 0
    sum_even = 0
    for j, digit in enumerate(str(number)):

        if j % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_odd == sum_even:
        print(number, end=' ')


