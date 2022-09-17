n = int(input())
count = 0
week = 0
print()
temp = []
for i in range(1, n + 1):
    temp.append(float(input(str(i) + ' день: ')))
    if temp[i - 1] < 23:
        count += 1
    else:
        break
        week = count / 7
print(week)