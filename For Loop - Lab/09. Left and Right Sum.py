n = int(input())
sum_left = 0
sum_right = 0

for i in range(1,n*2+1):
    if i <= n:
        sum_left += int(input())
    else:
        sum_right += int(input())


if sum_left == sum_right:
    print(f"Yes, sum = {sum_right}")
else:
    print(f"No, diff = {abs(sum_right-sum_left)}")
