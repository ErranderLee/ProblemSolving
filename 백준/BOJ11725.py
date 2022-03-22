import sys; read=sys.stdin.readline
import collections

n = int(read())
dict = collections.defaultdict(list)
visit = [0 for i in range(n + 1)]
answers = {}
for i in range(n-1):
    temp = list(map(int, read().rstrip().split()))
    dict[temp[0]].append(temp[1])
    dict[temp[1]].append(temp[0])
q = collections.deque()
q.append(1)
visit[1] = 1
answers[1] = -1

while q:
    node = q.popleft()
    for item in dict[node]:
        if visit[item] == 0:
            q.append(item)
            visit[item] = 1
            answers[item] = node
for i in range(2, n+1):
    print(answers[i])

