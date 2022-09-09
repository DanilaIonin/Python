y = int(input())
space = y - 1
star = 1
for i in range(1, y + 1):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2