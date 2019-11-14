import sys
import re


def my_lower(my_str):
    return my_str.lower()


def bring_properly_line(def_lines):
    def_lines = re.findall(r"[^,.!?:\ \n]+", def_lines)
    # def_lines = [my_string.lower() for my_string in def_lines]
    def_lines = list(map(my_lower, def_lines))
    return def_lines


my_lines = ""
with open(sys.argv[1], 'r') as file_read:
    my_lines = my_lines.join([line for line in file_read])
my_lines = bring_properly_line(my_lines)
print(my_lines)
my_lines_uniq = list(set(my_lines))
my_lines_uniq.sort()
[print("Verbs - ", i, " = ", my_lines.count(i))
 for i in my_lines_uniq]
