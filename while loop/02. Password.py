user = input()
password = input()

while True:
    new_pass=input()
    if new_pass == password:
        print(f"Welcome {user}!")
        break