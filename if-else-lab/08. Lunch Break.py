from math import ceil

tv_show = input()
time_episode = int(input())
time_off = int(input())
time_lunch = time_off / 8
time_relax = time_off / 4
needed_time = time_episode + time_lunch + time_relax

if time_off >= needed_time:
    print(f"You have enough time to watch {tv_show} and left with {ceil(time_off - needed_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show}, you need {ceil(needed_time - time_off)} more minutes.")

