lab_number = int(input("input number : "))
num_counters = range(1, (lab_number+1))
for num_counter in num_counters:
    if not lab_number % num_counter:
        print(num_counter)
