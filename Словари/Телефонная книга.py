while True:
    numbers = {}
    for z in range(int(input())):
        number = input().split()
        if number[1] not in numbers:
            numbers[number[1]] = []
        numbers[number[1]].append(number[0])
    for z in range(int(input())):
        name = input()
        if name in numbers:
            print(*numbers[name])
        else:
            print('Нет в телефонной книге')