from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for cloth in clothes:
        clothes_dict[cloth[1]].append(cloth[0])

    for value in clothes_dict.values():
        answer *= len(value) + 1

    return answer - 1