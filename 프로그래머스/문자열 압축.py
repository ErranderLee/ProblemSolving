import math

def solution(s):
    answer = 1001
    if len(s) == 1:
        return 1

    for i in range(1, math.floor(len(s)/2) + 1):
        count = 0
        answer_str = ''
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+2*i]:
                count += 1
            else:
                if count == 0:
                    answer_str += s[j:j+i]
                else:
                    answer_str += str(count+1) + s[j:j+i]
                    count = 0
        answer = min(answer, len(answer_str))
    return answer

print(solution("a"))