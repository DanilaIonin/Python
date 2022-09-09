price = float(input())
sum = 0
while price >= 0:
    if price >= 500:
        price = price - price * 0.07
    sum = sum + price
    price = float(input())
print(sum)