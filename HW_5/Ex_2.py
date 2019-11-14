import sys


def check_all(my_file, my_fizz, my_buzz, my_counter):
    my_file.write(check_fizz(my_fizz, my_counter))
    my_file.write(check_buzz(my_buzz, my_counter))
    my_file.write(check_counter(my_fizz, my_buzz, my_counter))
    my_file.write(" ")


def check_buzz(num_buzz, num_check):
    return "B" if num_check % num_buzz == 0 else ""


def check_fizz(num_fizz, num_check):
    return "F" if (not num_check % num_fizz) else ""


def check_counter(num_fizz, num_buzz, num_check):
    return(str(num_check)) if not num_check % num_buzz == 0 and num_check % num_fizz else ""


try:
    with open(sys.argv[1], 'r') as file_read:
        try:
            with open(sys.argv[2], 'w') as file_write:
                for line in file_read:
                    li = list(map(int, line.split()))
                    counters = range(1, (li[2]+1))
                    [check_all(file_write, li[0], li[1], counter)
                     for counter in counters]
                    file_write.write("\n")
        except IOError:
            print("An IOError has occurred with ", sys.argv[2])
except IOError:
    print("An IOError has occurred with ", sys.argv[1])
except IndexError:
    print("not enough arguments! Would be better if we have two :)")
