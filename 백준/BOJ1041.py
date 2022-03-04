import copy

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    arr.sort()
    print(sum(arr[:5]))
else:
    min = 250000000000000
    answer = 0
    candidates = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
    for candidate in candidates:
        tot = 0
        temp = []
        for i in range(3):
            temp.append(arr[candidate[i]])
        temp.sort()
        tot += n * n * temp[0]
        tot += 4 * temp[2] + (4*n-4) * temp[1]
        tot += 4 * temp[1] + (4*n-4) * temp[0]
        if tot < min:
            min = tot
            minList = copy.deepcopy(temp)
    answer += n * n * minList[0]
    answer += 4 * minList[2] + (4*n-4) * minList[1]
    for i in range(n-1, 0, -1):
        answer += 4 * minList[1] + (4*n-4) * minList[0]
    print(answer)
