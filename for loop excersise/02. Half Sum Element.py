sum_numbers = 0
max_num = float("-inf")
n = int(input())
for _ in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num
if sum_numbers == 2*max_num:
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(sum_numbers-2*max_num)}")


