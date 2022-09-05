import re, collections


def get_set(str):
    result = []
    reg = re.compile('[a-zA-Z]+')
    for i in range(len(str)-1):
        if reg.fullmatch(str[i:i+2]) is not None:
            result.append(str[i:i+2].lower())
    return result


def solution(str1, str2):
    answer = 0
    str1_set = get_set(str1)
    str2_set = get_set(str2)
    str1_counter = collections.Counter(str1_set)
    str2_counter = collections.Counter(str2_set)
    if len(str1_counter.keys()) == 0 and len(str2_counter.keys()) == 0:
        return 65536

    for key in str1_counter.keys():
        if key in str2_counter:
            answer += min(str1_counter[key], str2_counter[key])

    return int(answer / (len(str1_set) + len(str2_set) - answer) * 65536)