import sys
with open(sys.argv[1], 'r') as file_read:
    for my_line in file_read:
        my_line = my_line.split(";")
        nums_line = list(map(int, my_line[0].split()))
        bool_line = list(map(int, my_line[1].split()))
        [print(i, end=" ") for i in nums_line]
        print("", end="; ")
        [print(i, end=" ") for i in bool_line]
        if sum(nums_line)//len(nums_line) == bool_line[0] and sum(nums_line) % len(nums_line) == bool_line[1]:
            print("true")
        else:
            print("false")
