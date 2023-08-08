walked_steps = 0

while walked_steps < 10000:
    new_steps = input()
    if new_steps == "Going home":
        walked_steps += int(input())
        break
    walked_steps += int(new_steps)

if walked_steps < 10000:
    print(f"{10000 - walked_steps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!\n{walked_steps - 10000} steps over the goal!")
