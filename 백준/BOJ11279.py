import sys; read=sys.stdin.readline
import heapq;

n = int(read())
q = []
for i in range(n):
    inst = int(read().rstrip())
    if inst == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (-inst, inst))
