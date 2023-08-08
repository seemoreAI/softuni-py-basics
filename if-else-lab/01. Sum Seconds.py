time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_third + time_second + time_first

minutes = total_time // 60
seconds = total_time % 60

print(f'{minutes}:{seconds:02}')
