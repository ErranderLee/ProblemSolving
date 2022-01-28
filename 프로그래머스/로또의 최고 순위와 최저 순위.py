
def solution(lottos, win_nums):
    answer = []
    count = 0
    count_for_zero = 0
    for num in lottos:
        if num in win_nums:
            count += 1
        if num == 0:
            count_for_zero += 1
    best = 6 - (count + count_for_zero) + 1
    worst = 6 - count + 1
    answer.extend([best if best != 7 else 6, worst if worst != 7 else 6])
    return answer

print(solution([3, 2, 10, 5, 6, 1], [31, 10, 45, 1, 6, 19]))