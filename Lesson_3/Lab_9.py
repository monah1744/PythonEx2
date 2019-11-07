import sys
# filename = sys.argv[1]
# f = open(filename, 'r')
f = open(sys.argv[1], 'r')

for line in f:
    # li = line.split()
    # print(li)
    # li = list(map(int, li))
    li = [int(x) for x in line.split()]
    print(li)
f.close()
