list1 = [1, 2, 3]
list2 = list1  # Both list1 and list2 now point to the same list object

list2.append(4)
print(list1)  # Output: [1, 2, 3, 4]