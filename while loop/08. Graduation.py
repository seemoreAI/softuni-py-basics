name_student = input()
grade = 1
already_cut = False
average_grade = 0

while grade < 13:
    current_grade = float(input())
    if current_grade >= 4.00:
        average_grade += current_grade
        grade += 1
    else:
        if already_cut == True:
            print(f"{name_student} has been excluded at {grade} grade")
            break
        else:
            already_cut = True
else:
    grade = grade - 1
    print(f"{name_student} graduated. Average grade: {average_grade/grade:.2f}")
