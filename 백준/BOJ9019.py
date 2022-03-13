import sys
import collections
read = sys.stdin.readline

t = int(read())
questions = []
for i in range(t):
    temp = list(map(int, read().rstrip().split()))
    questions.append(temp)

for question in questions:
    visit = set()
    q = collections.deque()
    q.append([question[0], ''])
    visit.add(question[0])

    while q:
        node = q.popleft()
        if node[0] == question[1]:
            print(node[1])
            break
        temp = node[0] * 2 % 10000
        if temp not in visit:
            q.append([temp, node[1] + 'D'])
            visit.add(temp)

        if node[0] == 0:
            temp = 9999
        else:
            temp = node[0] - 1
        if temp not in visit:
            q.append([temp, node[1] + 'S'])
            visit.add(temp)

        temp = node[0]
        leftShift = 0
        leftShift += int(temp/1000)
        temp %= 1000
        leftShift += int(temp/100) * 1000
        temp %= 100
        leftShift += int(temp/10) * 100
        temp %= 10
        leftShift += int(temp/1) * 10
        if leftShift not in visit:
            q.append([leftShift, node[1] + 'L'])
            visit.add(leftShift)

        temp = node[0]
        rightShitf = 0
        rightShitf += int(temp / 1000) * 100
        temp %= 1000
        rightShitf += int(temp / 100) * 10
        temp %= 100
        rightShitf += int(temp / 10)
        temp %= 10
        rightShitf += int(temp / 1) * 1000
        if rightShitf not in visit:
            q.append([rightShitf, node[1] + 'R'])
            visit.add(rightShitf)


