import math

n = int(input())

five = math.floor(n/5)
answer = 0
for i in range(five, -1, -1):
    count = i
    res = n - i * 5
    if res % 3 == 0:
        count += res / 3
        answer = count
        break
    else:
        if i == 0:
            print(-1)
if answer != 0 : print(int(answer))