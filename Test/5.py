kids = 0
adults = 0

while True:
    age = input()
    if age == "Christmas":
        break
    age = int(age)
    if age <= 16:
        kids += 1
    else:
        adults += 1

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {kids*5}")
print(f"Money for sweaters: {adults*15}")



