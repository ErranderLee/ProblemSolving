def solution(numbers, target):
    answer = 0
    stack = list()
    candidates = []

    stack.extend([(-numbers[0], 1), (numbers[0], 1)])
    while stack:
        node = stack.pop()
        if node[1] + 1 == len(numbers):
            candidates.extend([node[0] - numbers[node[1]], node[0] + numbers[node[1]]])
        else:
            stack.extend([(node[0] - numbers[node[1]], node[1] + 1),
                          (node[0] + numbers[node[1]], node[1] + 1)])

    for candidate in candidates:
        if candidate == target:
            answer += 1
    return answer