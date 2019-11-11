import sys
import random
frases = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?",
          ", eh?", ", aw yea.", ", yo.", " No way!", ". Awesome!"]
with open(sys.argv[1], 'r') as file_read:
    for file_line in file_read:
        file_line.rstrip()
        print(file_line)
        li = [x for x in file_line.split(".")]
        print(li)
        for sentence in li:
            ##sentence += frases[random.randint(0, len(frases)-1)]
            print(sentence, end=(" "))
