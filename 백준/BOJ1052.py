n, k = list(map(int, input().split()))
first = 0
for i in range(0, 30):
    if 2**i <= n < 2**(i+1):
        first = i
        break
count = 0
lastRemain = 0
for i in range(first, -1, -1):
    if count == k:
        break
    if n == 0:
        print(0)
        exit(0)
    if n - 2**i >= 0:
        count += 1
        n -= 2**i
        lastRemain = 2**i
if n == 0:
    print(0)
else:
    print(lastRemain - n)