import sys
import heapq

n = int(input())
arr = []
sum = 0
acc = 0
for i in range(n):
    heapq.heappush(arr, int(sys.stdin.readline()))
if len(arr) == 1:
    print(0)
else:
    while True:
        acc = heapq.heappop(arr) + heapq.heappop(arr)
        sum += acc
        heapq.heappush(arr, acc)
        if len(arr) == 1:
            break
    print(sum)
