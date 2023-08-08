bad_marks_count = int(input())
problem_count = 0
sum_marks = 0
problem_name = ""
bad_marks = 0

while bad_marks < bad_marks_count:
    data = input()
    if data == "Enough":
        print(f"Average score: {sum_marks/problem_count:.2f}")
        print(f"Number of problems: {problem_count}")
        print(f"Last problem: {problem_name}")
        break
    else:
        problem_name = data
        mark = int(input())
        sum_marks += mark
        problem_count += 1
        if mark <= 4:
            bad_marks += 1
else:
    print(f"You need a break, {bad_marks} poor grades.")
