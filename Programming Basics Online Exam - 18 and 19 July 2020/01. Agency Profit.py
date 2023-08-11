company_name = input()
mature_tickets = int(input())
kid_tickets = int(input())
ticket_price = float(input())
tax = float(input())

kid_ticket_price = ticket_price * 0.3
ticket_price += tax
kid_ticket_price += tax
profit = (mature_tickets * ticket_price + kid_tickets * kid_ticket_price) * 0.2

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")

