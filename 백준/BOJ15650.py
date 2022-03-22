import itertools

n, m = list(map(int, input().split()))
arr = [i + 1 for i in range(n)]
answers = itertools.combinations(arr, m)
for answer in answers:
    for i in range(m):
        print(answer[i], end=' ')
    print()
