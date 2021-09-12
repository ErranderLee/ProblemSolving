
def solution(arr, minv, maxv):
    answers = []
    stack = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(0, maxv):
        visit = set()
        count = 0
        for x in range(len(arr)):
            for y in range(len(arr)):
                flag = 0
                if arr[x][y] <= i or (x, y) in visit:
                    pass
                else:
                    stack.append((x, y))
                    while stack:
                        flag = 1
                        node = stack.pop()
                        if node not in visit and arr[node[0]][node[1]] > i:
                            visit.add(node)
                            for d in range(4):
                                if 0 <= node[0] + dx[d] < len(arr) and 0 <= node[1] + dy[d] < len(arr):
                                    stack.append((node[0]+dx[d], node[1]+dy[d]))
                    if flag:
                        count += 1
        answers.append(count)

    return max(answers)


if __name__ == "__main__":
    num = int(input())
    arr = []
    minv = 101
    maxv= 0
    for i in range(num):
        temp = list(map(int, input().split()))
        arr.append(temp)
        tempmin = min(temp)
        tempmax = max(temp)
        minv = min(tempmin, minv)
        maxv = max(tempmax, maxv)
    print(solution(arr, minv, maxv))

