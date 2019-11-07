i = 10
while True:
    i -= 1
    if not i:
        continue
    if i % 2 == 0:
        print(i)
    if i < -10:
        break
