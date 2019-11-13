def my_qrt(my_num):
    if my_is_simple(my_num):
        return int(my_num*my_num)
    else:
        return int(my_num)


def my_is_simple(my_num):
    for i in range(2, int(my_num/2+2)):
        if my_num % i == 0:
            return False
    return True


my_numbers = list(range(1, 20))
print("numbers = ", my_numbers)
my_numbers = list(map(my_qrt, my_numbers))
print("new numbers = ", my_numbers)
# [print(my_qrt(my_n)) for my_n in my_numbers]
