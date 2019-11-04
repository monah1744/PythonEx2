num_fizz = int(input("Enter 1-st (fizz): "))
num_buzz = int(input("Enter 2-nd (buzz): "))
num_end_zz = int(input("Enter 3-rd (counters): "))

counter = 1

while counter <= num_end_zz:
    if not counter % num_fizz:
        print("F", end="")
    if counter % num_buzz == 0:
        print("B", end="")
    if not counter % num_buzz == 0 and counter % num_fizz:
        print(counter, end="")
    print("", end=" ")
    counter += 1
print()
