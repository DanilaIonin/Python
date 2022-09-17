z = int(input())
n = int(input())
print(0)
i = 1
s = n
for i in range(1, z):
    avr = s / i
    iq = int(input(str(i + 1)))
    if iq > avr:
        print('>')
    elif iq < avr:
        print('<')
    else:
        print(0)
        s += n