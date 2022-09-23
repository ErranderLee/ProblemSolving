from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    for num in course:
        word_count = defaultdict(int)
        for order in orders:
            order = sorted(order)
            splited = list(combinations(order, num))
            for element in splited:
                key = ''.join(element)
                word_count[key] += 1
        if word_count:
            max_value = max(word_count.values())
            for key, value in word_count.items():
                if value == max_value and value > 1:
                    answer.append(key)

    return sorted(answer)