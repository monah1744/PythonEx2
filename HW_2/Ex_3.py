def check_buzz(num_buzz, num_check):
    if num_check % num_buzz == 0:
        print("B", end="")


def check_fizz(num_fizz, num_check):
    if not num_check % num_fizz:
        print("F", end="")
    pass


num_fizz = int(input("Enter 1-st (fizz): "))
num_buzz = int(input("Enter 2-nd (buzz): "))
num_end_zz = int(input("Enter 3-rd (counters): "))

counters = range(1, (num_end_zz+1))
for counter in counters:
    check_buzz(num_buzz, counter)
    check_fizz(num_fizz, counter)
    # function for counter
    if not counter % num_buzz == 0 and counter % num_fizz:
        print(counter, end="")
    print("", end=" ")
print()
