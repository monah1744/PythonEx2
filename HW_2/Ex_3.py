def check_counter():
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
    # function for counter
    if not counter % num_buzz == 0 and counter % num_fizz:
        print(counter, end="")
    print("", end=" ")
print()
