
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
    answer.extend([best, worst if worst != 7 else 6])
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))