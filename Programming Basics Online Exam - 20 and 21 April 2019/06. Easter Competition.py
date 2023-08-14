kozunaks = int(input())
sum_marks = 0
max_mark = 0
winner = ""
for _ in range(kozunaks):
    chef = input()
    sum_marks = 0
    while True:
        mark = input()
        if mark == "Stop":
            print(f"{chef} has {sum_marks} points.")
            if sum_marks > max_mark:
                print(f"{chef} is the new number 1!")
                winner = chef
                max_mark = sum_marks
            break
        sum_marks += int(mark)
print(f"{winner} won competition with {max_mark} points!")


