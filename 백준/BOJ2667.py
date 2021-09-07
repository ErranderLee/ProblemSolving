
def solution(arr):
    answer = []
    stack = []
    visit = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count = 0
                stack.append((i, j))

                while stack:
                    node = stack.pop()
                    if node not in visit:
                        visit.append(node)
                        count += 1
                        if node[0]-1 >= 0 and arr[node[0]-1][node[1]] == 1:
                            stack.append((node[0]-1, node[1]))
                        if node[0]+1 < len(arr[i]) and arr[node[0]+1][node[1]] == 1:
                            stack.append((node[0]+1, node[1]))
                        if node[1]-1 >= 0 and arr[node[0]][node[1]-1] == 1:
                            stack.append((node[0], node[1]-1))
                        if node[1]+1 < len(arr[i]) and arr[node[0]][node[1]+1] == 1:
                            stack.append((node[0], node[1]+1))
                if count:
                    answer.append(count)

    return answer



if __name__ == "__main__":
    num = int(input())
    arr = list()
    for i in range(num):
        arr.append(list(map(int, input())))
    answer = solution(arr)
    answer.sort()
    count = len(answer)
    print(count)
    for item in answer:
        print(item)



