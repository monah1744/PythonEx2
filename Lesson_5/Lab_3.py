import sys
import re


def count_duplicates(def_list, def_index_start, def_index_finish):
    pass


def bring_properly_line(def_lines):
    def_lines = re.findall(r"[^,.!?:\ \n]+", def_lines)
    def_lines = [my_string.lower() for my_string in def_lines]
    def_lines.sort()
    return def_lines


# splited_string = re.findall(r'[^.!?]+', line_out)
my_lines = ""
with open(sys.argv[1], 'r') as file_read:
    my_lines = my_lines.join([line for line in file_read])
my_lines = bring_properly_line(my_lines)
print("Total - ", len(my_lines), "words", end="\n\n\n")
# i = count_duplicates(my_lines)
print(my_lines)
print("", end="\n\n\n")
[print("Verbs = ", my_lines[i], " ", my_lines.count(my_lines[i]))
 for i, _ in enumerate(my_lines)]
