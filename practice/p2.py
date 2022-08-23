import heapq
from collections import defaultdict


def solution(languages, scores):
    answer = []
    count_problems = len(scores[0])
    scores_per_language = defaultdict(list)
    avg_per_language = defaultdict(list)

    for language, score in zip(languages, scores):
        scores_per_language[language].append(score)
    for language in scores_per_language.keys():
        sum_of_score_per_language = [0] * count_problems
        for scores in scores_per_language[language]:
            for i, score in enumerate(scores):
                sum_of_score_per_language[i] += score
        for i in range(count_problems):
            avg_per_language[language].append(
                sum_of_score_per_language[i]/len(scores_per_language[language])
            )

    for i in range(count_problems):
        comparing_heap = []
        for language in scores_per_language.keys():
            str_sum = 0
            for ch in language:
                str_sum += ord(ch)
            infos_per_lang = (-avg_per_language[language][i], -len(scores_per_language[language]), -str_sum, language)
            heapq.heappush(comparing_heap, infos_per_lang)
        answer.append(heapq.heappop(comparing_heap)[-1])
    return answer


print(solution(
    ["C", "SWIFT", "JAVA", "SWIFT", "JAVA", "JAVA", "R"],
    [[65, 80, 90], [46, 100, 70], [91, 96, 59], [89, 90, 61], [0, 94, 75], [38, 95, 47], [50, 60, 90]]
               ))
print(solution(
    ["A", "AAA", "AA"],
    [[100, 50, 0, 30], [100, 50, 0, 25], [100, 50, 0, 30]]
))


