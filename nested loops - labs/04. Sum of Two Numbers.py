begin_number = int(input())
end_number = int(input())
magic_number = int(input())

combination_counter = 0

for i in range(begin_number, end_number + 1):
    for j in range(begin_number, end_number + 1):
        combination_counter += 1
        if i + j == magic_number:
            print(f"Combination N:{combination_counter} ({i} + {j} = {magic_number})")
            exit()
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")


