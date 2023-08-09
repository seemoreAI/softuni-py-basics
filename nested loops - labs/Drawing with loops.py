n=20
for i in range(1,n,2):
    print(((n - i) // 2) * " ",end="")
    for j in range(1,i+1):
        print("*",end='')
    print()
