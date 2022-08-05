import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        if scoville[0] >= K:
            return answer
        num_popped = heapq.heappop(scoville)
        top = heapq.heappop(scoville)
        heapq.heappush(scoville, max(num_popped * 2 + top, num_popped + 2 * top))
        answer += 1


print(solution([1, 2, 3, 9, 10, 12], 7))
