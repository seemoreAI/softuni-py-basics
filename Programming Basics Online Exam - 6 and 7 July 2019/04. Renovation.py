area = (int(input()) * int(input()) * 4)*(1-int(input())/100)

while True:
    command = input()
    if command == "Tired!":
        print(f"{int(area)} quadratic m left.")
        break
    area -= int(command)
    if area < 0:
        print(f"All walls are painted and you have {int(abs(area))} l paint left!")
        break
    if area == 0:
        print("All walls are painted! Great job, Pesho!")
        break

