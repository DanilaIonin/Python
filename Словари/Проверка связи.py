def slt(x):
    slovar[x] = slovar.get(x, 0) + 1
    return slovar[x]
slovar = {}
print(*[slt(k) for k in input().split()])

