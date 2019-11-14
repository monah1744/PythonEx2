def my_qrt(my_num):
    if my_is_simple(my_num):
        return int(my_num*my_num)
    else:
        return int(my_num)


def my_is_simple(my_num):
    if my_num == 2:
        return True
    if my_num == 1:
        return False
    for i in range(2, int(my_num/2+2)):
        if my_num % i == 0:
            return False
    return True


# my_numbers = list(range(1, 20))
my_numbers = [2, 3, 34, 17, 29, 6, 12, 3, 1, 4, 67, 98, 32, 5, 65, 7, 5, 4]
print("numbers = ", my_numbers)
my_numbers = list(map(my_qrt, my_numbers))
print("new numbers = ", my_numbers)
# [print(my_qrt(my_n)) for my_n in my_numbers]
