def has_only_odd_digits(num):
    # Check if a number has only odd digits
    return all(int(digit) % 2 != 0 for digit in str(num))

def print_numbers_with_only_odd_digits(begin_num, end_num):
    for num in range(begin_num, end_num + 1):
        if has_only_odd_digits(num):
            print(num, end=" ")

# Input
begin_num = int(input())
end_num = int(input())

# Call the function to print numbers with only odd digits
print_numbers_with_only_odd_digits(begin_num, end_num)