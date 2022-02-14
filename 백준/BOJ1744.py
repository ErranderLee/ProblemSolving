import sys
import heapq

n = int(input())
minus = []
plus = []
sum = 0
oneCount = 0
zeroCount = 0
for i in range(n):
    temp = int(sys.stdin.readline())
    if temp < 0:
        minus.append(temp)
    elif temp == 1:
        oneCount += 1
    elif temp == 0:
        zeroCount += 1
    else:
        plus.append(temp)
minus.sort()
plus.sort(reverse=True)

for i in range(0, len(minus), 2):
    if i+1 <= len(minus) - 1:
        sum += minus[i] * minus[i+1]

for i in range(0, len(plus), 2):
    if plus[i] != 0 and plus[i] != 1:
        if i+1 <= len(plus) - 1 and plus[i+1] != 0 and plus[i+1] != 1:
            sum += plus[i] * plus[i+1]
if len(plus) % 2 != 0:
    sum += plus[-1]
if len(minus) % 2 != 0:
    if zeroCount == 0:
        sum += minus[-1]
sum += oneCount

print(sum)
