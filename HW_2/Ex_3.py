print("Enter 1-st: ", end=" ")
num_fizz = int(input())

print("Enter 2-st: ", end=" ")
num_buzz = int(input())

print("Enter 3-st: ", end=" ")
num_end_zz = int(input())

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
