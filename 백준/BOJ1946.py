import sys

t = int(input())
answer = []
for i in range(t):
    n = int(input())
    temp = []
    arr1 = []
    arr2 = []
    count = 1
    for j in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
    arr1 = sorted(temp, key=lambda x:x[0])
    arr2 = sorted(temp, key=lambda x:x[1])
    core = sorted(arr2[0:arr1[0][1]-1], key=lambda x:x[0])
    if len(core) > 0:
        pos = core[0][1]
        count += 1
    for j in range(1, len(core)):
        if core[j][1] < pos:
            count += 1
            pos = core[j][1]
    answer.append(count)

for item in answer:
    print(item)
