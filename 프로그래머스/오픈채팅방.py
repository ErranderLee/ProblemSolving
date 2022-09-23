from collections import deque


def solution(record):
    answer = []
    q = deque()
    name_dict = dict()
    for inst in record:
        words = inst.split(' ')
        if len(words) == 3:
            method, uid, name = words
        else:
            method, uid = words
        if method == 'Enter':
            name_dict[uid] = name
            q.append((uid, method))
        elif method == 'Change':
            name_dict[uid] = name
        else:
            q.append((uid, method))
    while q:
        uid, method = q.popleft()
        if method == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(name_dict[uid]))
        else:
            answer.append("{}님이 나갔습니다.".format(name_dict[uid]))
    return answer