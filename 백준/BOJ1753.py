import sys; read=sys.stdin.readline
import heapq
from collections import defaultdict

inf = 9876754321
v, e = list(map(int, read().rstrip().split()))
start = int(read())
graph = defaultdict(list)
distance = [inf for i in range(v+1)]

for i in range(e):
    s, e, cost = list(map(int, read().rstrip().split()))
    graph[s].append((cost, e))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue
    for nextNode in graph[node]:
        cost = nextNode[0] + distance[node]
        if cost < distance[nextNode[1]]:
            distance[nextNode[1]] = cost
            heapq.heappush(q, (cost, nextNode[1]))
for i in range(1, len(distance)):
    if distance[i] != inf:
        print(distance[i])
    else:
        print('INF')
