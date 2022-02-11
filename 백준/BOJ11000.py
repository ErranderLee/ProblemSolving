import sys
import copy
import heapq

n = int(input())
classes = []
q = []
for i in range(n):
    classes.append(list(map(int, sys.stdin.readline().split())))

classes.sort()
heapq.heappush(q, classes[0][1])

for i in range(1, n):
    if q[0] <= classes[i][0]:
        heapq.heappop(q)
        heapq.heappush(q, classes[i][1])
    else:
        heapq.heappush(q, classes[i][1])
print(len(q))