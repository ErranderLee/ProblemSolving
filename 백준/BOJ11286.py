import sys; read = sys.stdin.readline
import heapq

n = int(read())
heap = []
for i in range(n):
    x = int(read())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
