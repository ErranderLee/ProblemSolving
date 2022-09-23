import itertools
import collections
import sys


def solution(n, info):
    answer = []
    info.reverse()
    scores = [i for i in range(11)]
    candidates = list(itertools.combinations_with_replacement(scores, n))
    apeach = 0
    max_diff = -sys.maxsize
    for candidate in candidates:
        lion = 0
        apeach = 0
        counter = collections.Counter(candidate)
        result = [0 for i in range(11)]
        for i in range(0, 11):
            if i in counter:
                if counter[i] > info[i]:
                    lion += i
                    result[i] = counter[i]
                else:
                    apeach += i
            else:
                if info[i] != 0:
                    apeach += i
        diff = lion - apeach
        if max_diff < diff:
            answer = result
            max_diff = diff

    if max_diff <= 0:
        return [-1]
    temp = n - sum(answer)
    if temp == 0:
        return answer[::-1]
    answer[0] = temp
    return answer[::-1]