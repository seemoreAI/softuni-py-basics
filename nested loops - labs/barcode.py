my_begin = input()
my_end = input()

for i in range(int(my_begin[0]), int(my_end[0])+1):
    for j in range(int(my_begin[1]), int(my_end[1])+1):
        for k in range(int(my_begin[2]), int(my_end[2])+1):
            for m in range(int(my_begin[3]), int(my_end[3])+1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and m % 2 !=0:
                    print(f"{i}{j}{k}{m}")

