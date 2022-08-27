from collections import deque


def is_changable(popped_word, word):
    count = 0
    length = len(word)
    for i in range(length):
        if popped_word[i] != word[i]:
            count += 1
            if count > 1:
                return False
    return True


def solution(begin, target, words):
    answer = 0
    visit = [0] * len(words)
    q = deque()
    q.append((begin, 0))

    if target not in words:
        return answer

    while q:
        popped_word, count = q.popleft()
        for i in range(len(words)):
            if visit[i] != 1 and is_changable(popped_word, words[i]):
                if words[i] == target:
                    return count + 1
                q.append((words[i], count + 1))
                visit[i] = 1

    return answer
