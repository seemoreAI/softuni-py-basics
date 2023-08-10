total_tickets = 0
student_tickets_t = 0
standard_tickets_t = 0
kid_tickets_t = 0
while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    free_seats = int(input())
    kid_tickets = 0
    student_tickets = 0
    standard_tickets = 0
    for i in range(1,free_seats+1):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "kid":
            kid_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
    total_tickets += student_tickets + standard_tickets + kid_tickets
    student_tickets_t += student_tickets
    standard_tickets_t += standard_tickets
    kid_tickets_t += kid_tickets
    print(f"{movie_name} - {(student_tickets + standard_tickets + kid_tickets) / free_seats * 100:.2f}% full.")
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_t/total_tickets*100:.2f}% student tickets.")
print(f"{standard_tickets_t/total_tickets*100:.2f}% standard tickets.")
print(f"{kid_tickets_t/total_tickets*100:.2f}% kids tickets.")
