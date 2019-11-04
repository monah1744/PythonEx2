def check_counter(num_fizz, num_buzz, num_check):
    if not num_check % num_buzz == 0 and num_check % num_fizz:
        print(num_check, end="")
    pass


num_fizz = int(input("Enter 1-st (fizz): "))
num_buzz = int(input("Enter 2-nd (buzz): "))
num_end_zz = int(input("Enter 3-rd (counters): "))

counters = range(1, (num_end_zz+1))
for counter in counters:
    # function for fizz
    if not counter % num_fizz:
        print("F", end="")
    # function for buzz
    if counter % num_buzz == 0:
        print("B", end="")
    check_counter(num_fizz, num_buzz, counter)
    print("", end=" ")
print()
