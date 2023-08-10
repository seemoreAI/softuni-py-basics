n = int(input())
m = 1
is_bigger = False

for i in range(1,n+1):
    for j in range(1,i+1):
        print(m, end=' ')
        if m == n:
            is_bigger = True
            break
        m += 1
    if is_bigger:
        break
    print()
