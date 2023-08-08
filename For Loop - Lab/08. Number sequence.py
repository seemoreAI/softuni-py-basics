n = int(input())
max_num = float('-inf')
min_num = float('inf')
print(max_num)
for i in range(n):
    num = int(input())
    max_num = max(max_num, num)
    min_num = min(min_num, num)

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')