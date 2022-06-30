from itertools import combinations
from itertools import permutations

def findPrime(candidateNumbers):
    count = 0
    for candidateNumber in candidateNumbers:
        if candidateNumber != 1 and candidateNumber != 0:
            count += 1
            for i in range(2, candidateNumber):
                if candidateNumber % i == 0:
                    count -= 1
                    break
    return count

def toInteger(candidateNumber):
    temp = ""
    return int(temp.join(candidateNumber))

def solution(numbers):
    answer = 0
    candidates = list()

    for i in range(1, len(numbers) + 1):
        candidates.extend(combinations(numbers, i))
    candidates = list(set(candidates))

    candidateNumbers = list()
    for candidate in candidates:
        temp = list(permutations(candidate, len(candidate)))

        for candidateNumber in temp:
            candidateNumbers.append(toInteger(candidateNumber))

    return findPrime(list(set(candidateNumbers)))