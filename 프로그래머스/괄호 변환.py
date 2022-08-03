
def divide_into_balanced_str(p):
    sum = 0
    for i, ch in enumerate(p):
        if ch == '(':
            sum += 1
        else:
            sum -= 1
        if sum == 0:
            u = p[:i+1]
            v = p[i+1:]
            return u, v

def check_right_str(p):
    stack = []
    if p[0] == ')':
        return False
    for ch in p:
        if stack and stack[-1] == '(' and ch == ')':
            stack.pop()
        else:
            stack.append(ch)
    if stack:
        return False
    return True

def solution(p):
    answer = ""
    if len(p) == 0:
        return ""
    u, v = divide_into_balanced_str(p)
    if check_right_str(u):
        answer = u + solution(v)
        return answer
    else:
        temp = "("
        temp += solution(v)
        temp += ")"
        u = u[1:len(u)-1]
        for i, ch in enumerate(u):
            if ch == '(':
                temp += ')'
            else:
                temp += '('
        return temp

print(solution("()))((()"))