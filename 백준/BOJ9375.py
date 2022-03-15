import sys
import collections
read = sys.stdin.readline

t = int(read())
answers = []
for i in range(t):
    n = int(read())
    wears = collections.defaultdict(list)
    for j in range(n):
        temp = read().rstrip().split()
        wears[temp[1]].append(temp[0])
    sum = 1
    for j in wears.keys():
        sum *= len(wears[j]) + 1
    answers.append(sum - 1)
for answer in answers:
    print(answer)
