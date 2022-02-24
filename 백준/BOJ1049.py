import sys

broken, numBrand = list(map(int, sys.stdin.readline().split()))
prices = []
sum = 0
for i in range(numBrand):
    prices.append(list(map(int, sys.stdin.readline().split())))

prices1 = sorted(prices, key=lambda x:x[0])
prices2 = sorted(prices, key=lambda x:x[1])

if broken <= 6:
    sum += min(broken * prices2[0][1], prices1[0][0])
else:
    if 6 * prices2[0][1] > prices1[0][0]:
        sum += int(broken / 6) * prices1[0][0]
        if (broken % 6) * prices2[0][1] > prices1[0][0]:
            sum += prices1[0][0]
        else:
            sum += broken % 6 * prices2[0][1]
    else:
        sum += prices2[0][1] * broken
print(sum)