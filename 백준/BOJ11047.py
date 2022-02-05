import math

n, k = map(int, input().split())
values = []
for i in range(n):
    values.append(int(input()))

values.reverse()
start = 0
count = 0

if n == 1:
    count += math.floor(k/values[0])
else:
    for i in range(0, len(values) - 1):
        if i == 0:
            if k >= values[i]:
                count += math.floor(k / values[i])
                k = k % values[i]
        if values[i] > k and k >= values[i+1]:
            count += math.floor(k/values[i+1])
            k = k % values[i+1]
print(count)

