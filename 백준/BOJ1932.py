import sys
import collections

n = int(input())
triangle = collections.defaultdict(list)

for i in range(n):
    triangle[i].extend(list(map(int, sys.stdin.readline().rstrip().split())))

if n == 1:
    print(triangle[0][0])
elif n == 2:
    print(triangle[0][0] + max(triangle[1]))
else:
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]
    for i in range(2, n):
        for j in range(0, i + 1):
            if j == 0:
                triangle[i][0] += triangle[i - 1][0]
            elif j == i:
                triangle[i][i] += triangle[i - 1][i - 1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    print(max(triangle[n-1]))




