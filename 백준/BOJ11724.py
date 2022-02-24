import sys
import collections
n, m = list(map(int, sys.stdin.readline().rstrip().split()))
edges = collections.defaultdict(list)
visit = [0] * n
stack = []
count = 1
for i in range(m):
    u, v = list(map(int, sys.stdin.readline().rstrip().split()))
    edges[u].append(v)
    edges[v].append(u)

stack.append(1)
visit[0] = 1
while 0 in visit:
    while len(stack):
        popNode = stack.pop()
        for node in edges[popNode]:
            if visit[node-1] == 0:
                stack.append(node)
                visit[node-1] = 1

    for i in range(len(visit)):
        if visit[i] == 0:
            count += 1
            stack.append(i+1)
            visit[i] = 1
            break
print(count)
