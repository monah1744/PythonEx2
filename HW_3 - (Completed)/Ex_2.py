import sys


def check_buzz(num_buzz, num_check):
    if num_check % num_buzz == 0:
        return("B")
    else:
        return ""


def check_fizz(num_fizz, num_check):
    if not num_check % num_fizz:
        return("F")
    else:
        return ""


def check_counter(num_fizz, num_buzz, num_check):
    if not num_check % num_buzz == 0 and num_check % num_fizz:
        return(str(num_check))
    else:
        return ""


###f = open(input("input filename for reading : "), 'r')
##f = open(sys.argv[1], 'r')
print(len(sys.argv), "argument")

try:
    with open(sys.argv[1], 'r') as file_read:
        for line in file_read:
            li = [int(x) for x in line.split()]
            counters = range(1, (li[2]+1))
            for counter in counters:
                print(check_buzz(li[0], counter), end="")
                print(check_fizz(li[1], counter), end="")
                print(check_counter(li[0], li[1], counter), end="")
                print(" ", end="")
            print("\n")
except IOError:
    print("An IOError has occurred!")
except IndexError:
    print("not enough arguments! Would be better if we have two :)")
