budget = float(input())
nights = int(input())
price = float(input())
additional_expenses = int(input())

if nights > 7:
    price = price - 0.05*price
total_price = price * nights + additional_expenses/100 * budget
diff = f"{abs(total_price - budget):.2f}"
if total_price <= budget:
    print(f"Ivanovi will be left with {diff} leva after vacation.")
else:
    print(f"{diff} leva needed.")





