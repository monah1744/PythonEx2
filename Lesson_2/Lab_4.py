x = int(input("input number : "))
y = 0
while x > 0:
    print(x % 10, " * 10^", y)
    y += 1
    x = x // 10
