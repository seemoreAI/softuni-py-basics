wanted_book = input()
i = 0
while True:
    book = input()
    if book == wanted_book:
        print(f"You checked {i} books and found it.")
        break
    if book == "No More Books":
        print(f"The book you search is not here!\nYou checked {i} books.")
        break
    i += 1
