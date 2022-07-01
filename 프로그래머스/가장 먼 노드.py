from collections import deque, defaultdict

def list_to_dict(edge):
    edge_dict = defaultdict(list)
    for element in edge:
        edge_dict[element[0]].append(element[1])
        edge_dict[element[1]].append(element[0])
    return edge_dict

def count_farthest_nodes(visit):
    max_distance = max(visit)
    count = 0
    for distance in visit:
        if distance == max_distance:
            count += 1
    return count

def solution(n, edge):
    answer = 0
    visit = [0] * (n+1)
    edge_dict = list_to_dict(edge)

    q = deque()
    q.append(1)
    visit[1] += 1
    while q:
        node = q.popleft()
        for target in edge_dict[node]:
            if visit[target] == 0:
                q.append(target)
                visit[target] = visit[node] + 1

    return count_farthest_nodes(visit)