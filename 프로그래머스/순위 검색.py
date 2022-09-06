from collections import defaultdict
from itertools import combinations
import bisect


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    combs = []
    for i in range(0, 5):
        combs.append(list(combinations([0, 1, 2, 3], i)))
    for element in info:
        temp = element.split(' ')
        for comb in combs:
            for tup in comb:
                key = [temp[num] for num in range(4)]
                for index in tup:
                    key[index] = '-'
                info_dict[tuple(key)].append(int(temp[-1]))
    for key in info_dict:
        info_dict[key].sort()
    for element in query:
        q = element.split(' and ')
        count = 0
        q.extend(q.pop().split(' '))
        temp = info_dict[tuple(q[:-1])]
        score = int(q[-1])
        result = 0
        index = bisect.bisect_left(temp, score)
        answer.append(len(temp) - index)

    return answer