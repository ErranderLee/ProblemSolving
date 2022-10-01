from collections import defaultdict, deque
from itertools import combinations


def create_candidates(nodes, n):
    result = defaultdict(list)
    temp = list(combinations(nodes, n))
    for cand in temp:
        result[1].append(cand)
        result[2].append(list(set(nodes).difference(set(cand))))
    return result


def calc_diff(area1, area2, graph, populations, n):
    area1_pops = check_is_possible_and_calc_pops(area1, graph, populations, n)
    area2_pops = check_is_possible_and_calc_pops(area2, graph, populations, n)
    if area2_pops[0] and area1_pops[0]:
        return [True, abs(area1_pops[1] - area2_pops[1])]
    else:
        return [False, 0]


def check_is_possible_and_calc_pops(area, graph, populations, n):
    pops = 0
    visit = [False for i in range(n)]
    q = deque()
    q.append(area[0])
    visit[area[0]] = True
    pops += populations[area[0]]
    while q:
        node = q.popleft()
        for next in graph[node]:
            if not visit[next] and next in area:
                visit[next] = True
                pops += populations[next]
                q.append(next)
    for node in area:
        if not visit[node]:
            return [False, 0]
    return [True, pops]


if __name__ == '__main__':
    n = int(input())
    populations = list(map(int, input().split()))
    graph = defaultdict(list)
    nodes = [i for i in range(n)]
    answer = 1e9
    for i in range(n):
        temp = list(map(int, input().split()))
        for node in temp[1:]:
            graph[i].append(node - 1)
            graph[node - 1].append(i)

    for i in range(1, n):
        candidates = create_candidates(nodes, i)
        for j in range(len(candidates[1])):
            is_possible, diff = calc_diff(candidates[1][j], candidates[2][j], graph, populations, n)
            if is_possible:
                answer = min(answer, diff)
    if answer == 1e9:
        print(-1)
    else:
        print(answer)


