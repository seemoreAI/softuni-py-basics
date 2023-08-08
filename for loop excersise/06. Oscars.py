name = input()
points = float(input())
n = int(input())
needed_points = 1250.5

for i in range(n):
    tester_name = input()
    tester_points = float(input())
    points += len(tester_name)*tester_points/2
    if points > needed_points:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {name} you need {needed_points - points:.1f} more!")