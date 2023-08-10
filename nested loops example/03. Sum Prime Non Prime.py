sum_prime = 0
sum_non_prime = 0

while True:
    data = (input())
    if data == "stop":
        break
    data = int(data)
    if data < 0:
        print("Number is negative.")
        continue
    for i in range(2,data//2+1):
        if data % i == 0:
            sum_non_prime += data
            break
    else:
        sum_prime += data
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")

