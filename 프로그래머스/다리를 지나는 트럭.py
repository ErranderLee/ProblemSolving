from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    sum = 0
    for truck_weight in truck_weights:
        if sum + truck_weight <= weight:
            sum -= bridge.popleft()
            sum += truck_weight
            bridge.append(truck_weight)
            answer += 1
        else:
            while True:
                sum -= bridge.popleft()
                answer += 1
                if sum + truck_weight <= weight:
                    sum += truck_weight
                    bridge.append(truck_weight)
                    break
                else:
                    bridge.append(0)
    while sum:
        sum -= bridge.popleft()
        answer += 1

    return answer
