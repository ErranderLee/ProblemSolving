import copy
import itertools
global answer
answer = set()
input_str = list(input())

def rec(str):
    global answer
    indice = []
    count = 0
    count_open = 0
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(['(', i])
            count_open += 1
        elif str[i] == ')':
            index = stack.pop()[1]
            indice.append([i, index])
            count += 1

    if count_open == 0:
        return

    for i in range(1, count_open + 1):
        comb = itertools.combinations([i for i in range(count_open)], i)
        for j in comb:
            temp = str[:]
            for k in j:
                for a in indice[k]:
                    temp[a] = ''
            answer.add(''.join(temp))

rec(input_str)
for item in sorted(list(answer)):
    print(item)


