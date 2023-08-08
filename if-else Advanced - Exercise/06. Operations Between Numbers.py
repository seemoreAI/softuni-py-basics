n1, n2 = int(input()), int(input())
oper = input() # "+", "-", "*", "/", "%".
result = 0

if oper == "+" or oper == "-" or oper == "*":
    if oper == "+":
        result = n1 + n2
    elif oper == "-":
        result = n1 - n2
    elif oper == "*":
        result = n1 * n2

    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    print(f"{n1} {oper} {n2} = {result} - {even_or_odd}")
elif (oper == "/" or oper == "%") and n2 != 0:
    if oper == "/":
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
else:
    print(f"Cannot divide {n1} by zero")

