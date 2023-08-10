n = int(input())
m = int(input())
sum_odd = 0
sum_even = 0

for i in range(n, m+1):
    for j in range(0,len(str(n)),2):
        str_i = str(i)
        sum_odd += int(str_i[j])
        sum_even += int(str_i[j+1])
    if sum_odd == sum_even:
        print(i, end=' ')
    sum_odd = 0
    sum_even = 0

