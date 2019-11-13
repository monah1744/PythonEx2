def line_up(my_line):
    my_line = str(my_line)
    return my_line.upper()


def line_down(my_line):
    my_line = str(my_line)
    return my_line.lower()


line1 = input("input line 1 : ")
print(line1)
############################################

lines1 = line1.split()
lines1 = list(map(line_up, lines1))
print(lines1)
lines1 = list(map(line_down, lines1))
print(lines1)
