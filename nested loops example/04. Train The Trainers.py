n = int(input())
average_mark_student_sum = 0
marks = 0

while True:
    presentation_name = input()
    sum_mark=0
    if presentation_name == "Finish":
        break
    for _ in range(n):
        mark=float(input())
        sum_mark += mark
        average_mark_student_sum += mark
        marks += 1
    print(f"{presentation_name} - {sum_mark/n:.2f}.")
print(f"Student's final assessment is {average_mark_student_sum/marks:.2f}.")
