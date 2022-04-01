import sys; read=sys.stdin.readline
from collections import defaultdict
import heapq
inf = 987654321
v = int(read())
e = int(read())
graph = defaultdict(list)
distance = [inf for i in range(v+1)]

for i in range(e):
    start, end, cost = list(map(int, read().rstrip().split()))
    graph[start].append((end, cost))
startNode, endNode = list(map(int, read().rstrip().split()))

def dijkstra(startNode):
    q = []
    heapq.heappush(q, (0, startNode))
    distance[startNode] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for nextNode in graph[node]:
            cost = distance[node] + nextNode[1]
            if cost < distance[nextNode[0]]:
                distance[nextNode[0]] = cost
                heapq.heappush(q, (cost, nextNode[0]))
dijkstra(startNode)
print(distance[endNode])