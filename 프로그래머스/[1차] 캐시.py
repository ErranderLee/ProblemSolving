from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    answer = 0
    q = deque(maxlen=cacheSize)

    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    for city in cities:
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            q.append(city)

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))