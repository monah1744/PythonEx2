import sys
import random

frases = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?",
          ", eh?", ", aw yea.", ", yo.", " No way!", ". Awesome!"]
with open(sys.argv[1], 'r') as file_read:
    for file_line in file_read:
        end_li = len(file_line)
        while file_line.rfind(".", 0, end_li) >= 0:
            finded_index = file_line.rfind(".", 0, end_li)
            file_line = file_line[:finded_index] + frases[random.randint(
                0, len(frases)-1)] + file_line[(finded_index+1):]
            end_li = finded_index-1 if finded_index else 0
        print(file_line, end="")
