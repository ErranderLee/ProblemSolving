import heapq


def solution(n, works):
    answer = 0
    work_max_heap = []
    if sum(works) <= n:
        return 0
    for work in works:
        heapq.heappush(work_max_heap, (-work, work))
    while n > 0:
        popped = heapq.heappop(work_max_heap)
        heapq.heappush(work_max_heap, (popped[0] + 1, popped[1] - 1))
        n -= 1
    for minus_work, work in work_max_heap:
        answer += work**2

    return answer