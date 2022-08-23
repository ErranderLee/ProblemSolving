from collections import defaultdict
from itertools import combinations


def search(graph, candidate):
    stack = []
    candidate = list(candidate)
    candidate.sort()
    stack.append(candidate[0])
    while stack:
        node = stack.pop()
        for lot in graph[node]:
            if lot == candidate[1]:
                return False
            stack.append(lot)
    return True


def solution(parking):
    answer = 0
    parking_lots = [i for i in range(len(parking))]
    graph = defaultdict(list)

    for i, connections in enumerate(parking):
        for connection in connections:
            if connection != -1:
                graph[i].append(connection)
    candidates = list(combinations(parking_lots, 2))
    for candidate in candidates:
        if search(graph, candidate):
            answer += 1

    return answer


print(solution([[1,2],[3,4],[-1,-1],[-1,-1],[-1,-1]]))
print(solution([[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]))