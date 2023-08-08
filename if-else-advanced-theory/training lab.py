w,h = float(input()), float(input())

w= w*100
h= h*100 - 100
count_w = w // 120
count_h = h // 70
count = count_h * count_w -3
print(int(count))
