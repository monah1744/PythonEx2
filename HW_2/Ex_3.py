# input first - fizz
num_fizz = int(input("Enter 1-st (fizz): "))
# input second - buzz
num_buzz = int(input("Enter 2-nd (buzz): "))
# input Last - counters
num_end_zz = int(input("Enter 3-rd (counters): "))

counters = range(1, (num_end_zz+1))
for counter in counters:
    if not counter % num_fizz:
        print("F", end="")
    if counter % num_buzz == 0:
        print("B", end="")
    if not counter % num_buzz == 0 and counter % num_fizz:
        print(counter, end="")
    print("", end=" ")
print()
