import heapq
import collections
import sys


def dijikstra(start, fares_list, node_graph, n):
    dists = [sys.maxsize for i in range(n + 1)]
    dists[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > dists[node]:
            continue
        for next in node_graph[node]:
            cost = dist + fares_list[node][next]
            if cost < dists[next]:
                dists[next] = cost
                heapq.heappush(q, (cost, next))
    return dists

def solution(n, s, a, b, fares):
    answer = 0
    fares_list = [[0 for i in range(n + 1)] for j in range(n + 1)]
    node_graph = collections.defaultdict(list)

    for fare in fares:
        fares_list[fare[0]][fare[1]] = fare[2]
        fares_list[fare[1]][fare[0]] = fare[2]
        node_graph[fare[0]].append(fare[1])
        node_graph[fare[1]].append(fare[0])
    start_sht_dists = dijikstra(s, fares_list, node_graph, n)
    answer = sys.maxsize
    for i in range(1, n + 1):
        total = 0
        total += start_sht_dists[i]
        total += dijikstra(i, fares_list, node_graph, n)[a]
        total += dijikstra(i, fares_list, node_graph, n)[b]
        answer = min(answer, total)
    return answer