import sys
import heapq

n, k = list(map(int, input().split()))
jewels = []
bags = []
total_val = 0

for i in range(n):
    heapq.heappush(jewels, list(map(int, sys.stdin.readline().split())))
for i in range(k):
    bags.append(int(sys.stdin.readline()))

bags.sort()

temp = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewels)[1])
    if temp:
        total_val += heapq.heappop(temp)
    elif not jewels:
        break
print(-total_val)
