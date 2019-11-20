def spam(number):
    res = "".join(['bulochka' for i in range(number)])
    return res


def my_sum(list_of_numbers):
    my_summ = 0
    for my_numm in list_of_numbers:
        my_summ += my_numm
    return my_summ


def shortener(string):
    my_new_string = ""
    for my_string in string.split():
        if len(my_string) > 6:
            my_new_string = my_new_string + my_string[:6] + "* "
        else:
            my_new_string = my_new_string + my_string + " "
    return my_new_string.rstrip()


def compare_ends(words):
    counter = [1 for my_word in words if len(
        my_word) >= 2 and my_word[0] == my_word[len(my_word)-1]]
    return len(counter)
