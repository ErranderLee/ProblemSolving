from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = deque()
    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100-progress)/speed))

    stack = list()
    stack.append(days.popleft())
    while days:
        node = stack.pop()
        count = 1
        while True:
            if days and node >= days[0]:
                days.popleft()
                count += 1
            else:
                if days:
                    stack.append(days.popleft())
                answer.append(count)
                break
    if stack:
        answer.append(1)

    return answer