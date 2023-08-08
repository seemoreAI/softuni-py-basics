nylon = int(input())
paint = int(input())
razreditel = int(input())
hours = int(input())

SUM_TORBICHKI= 0.4



sum_nylon=(nylon+2) * 1.5
sum_paint = paint*1.1*14.5
sum_razreditel = razreditel*5
sum_materiali = sum_razreditel +sum_nylon +sum_paint + SUM_TORBICHKI
sum_work =  (sum_materiali * 0.3) * hours
sum = sum_work + sum_materiali

print(sum)
