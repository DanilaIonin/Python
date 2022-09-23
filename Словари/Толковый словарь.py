while True:
    x = int(input())
    slovar = {}
    for a in range(x):
        words = input().split()
        word = words[0]
        xxx = words[1:len(words) + 1]
        slovar[word] = xxx
    for a in range(int(input())):
        word = input()
        if word not in slovar:
            print('Нет в словаре')
        else:
            print(*slovar[word])