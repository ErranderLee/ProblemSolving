def check(str, stack):
    for ch in str:
        if ch == '(' or ch == '[':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return 0
            else:
                if ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return 0
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return 0
    if len(stack) > 0:
        return 0
    return 1

str = input()
stack = []
flag = check(str, stack)

str = list(str[::-1])

def rec(ch):
    sum = 0
    while str:
        val = str.pop()
        if val == '(' or val == '[':
            sum += rec(val)
        elif ch == '(' and val == ')':
            return 2 * max(1, sum)
        elif ch == '[' and val == ']':
            return 3 * max(1, sum)
    return sum
if flag:
    sum = rec('')
    print(sum)
else:
    print(0)
    exit()