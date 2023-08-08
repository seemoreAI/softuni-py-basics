n = int(input())
sum_left = 0
sum_right = 0

for i in range(n):
    if i % 2 == 0:
        sum_left += int(input())
    else:
        sum_right += int(input())


if sum_left == sum_right:
    print("Yes")
    print(f"Sum = {sum_right}")

else:
    print("No")
    print(f"Diff = {abs(sum_right-sum_left)}")

