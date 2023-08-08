pages_to_read = int(input())
pages_for_hour=int(input())
days_for_book=int(input())

needed_hours=pages_to_read//pages_for_hour
hours_per_day=needed_hours//days_for_book

print(hours_per_day)