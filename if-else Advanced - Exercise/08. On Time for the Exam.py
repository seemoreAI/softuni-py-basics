hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

condition = ""

total_exam = hour_exam * 60 + minute_exam
total_arrive = hour_arrive * 60 + minute_arrive

if total_arrive > total_exam:
    condition = "Late"
elif total_arrive < total_exam - 30:
    condition = "Early"
else:
    condition = "On time"

print(condition)

if total_arrive < total_exam:
    if total_exam - total_arrive < 60:
        mm = (total_exam - total_arrive)
        print(f'{mm} minutes before the start')
    else:
        hh = (total_exam - total_arrive) // 60
        mm = (total_exam - total_arrive) % 60
        print(f'{hh}:{mm:02d} hours before the start')
elif total_arrive > total_exam:
    if total_arrive - total_exam  < 60:
        mm = (total_arrive - total_exam )
        print(f'{mm} minutes after the start')
    else:
        hh = abs(total_exam - total_arrive) // 60
        mm = abs(total_exam - total_arrive) % 60
        print(f'{hh}:{mm:02d} hours after the start')


