import collections
import heapq


def dijikstra(graph, start, n):
    costs = [100000000 for _ in range(n + 1)]
    costs[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, node = heapq.heappop(q)
        if cost > costs[node]:
            continue
        for next in graph[node]:
            new_cost = next[1] + costs[node]
            if new_cost < costs[next[0]]:
                heapq.heappush(q, (new_cost, next[0]))
                costs[next[0]] = new_cost
    return costs


n, m, x = map(int, input().rstrip().split())
graph = collections.defaultdict(list)
for i in range(m):
    a, b, t = map(int, input().rstrip().split())
    graph[a].append((b, t))
dist = []
for i in range(1, n + 1):
    dist.append(dijikstra(graph, i, n))
way_back = dijikstra(graph, x, n)
cand = []
for i in range(n):
    cand.append(dist[i][x] + way_back[i + 1])
print(max(cand))


