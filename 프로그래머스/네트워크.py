
def solution(n, computers):
    visit = [0] * n
    stack = list()
    count = 0
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            stack.append(i)
            count += 1
            while stack:
                node = stack.pop()
                for j in range(n):
                    if visit[j] == 0 and computers[node][j] == 1:
                        stack.append(j)
                        visit[j] = 1
    return count