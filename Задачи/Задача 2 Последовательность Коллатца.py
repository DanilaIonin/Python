while True:
    a = int(input())
    sum = 0
    while a != 1:
        if a % 2 == 0:
            a = a / 2
            sum += 1
        else:
            a = 3 * a + 1
            sum += 1
    print(sum)
