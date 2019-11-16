my_num = -1
while my_num <= 0 or not my_num % 2:
    my_num = int(input("enter odd number - "))

print(my_num)
for i in range(1, my_num+1, 2):
    my_line = "*"*i
    my_line = my_line.center(my_num, " ")
    print(my_line)
for i in range(my_num-2, 0, -2):
    my_line = "*"*i
    my_line = my_line.center(my_num, " ")
    print(my_line)
