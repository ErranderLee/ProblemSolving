import sys; read=sys.stdin.readline

s = read().rstrip()
t = read().rstrip()
stack = []

if len(s) < len(t):
    print(s)
else:
    t = list(t)
    for ch in s:
        stack.append(ch)
        if ch == t[-1]:
            if stack[len(stack)-len(t):] == t:
                for i in range(len(t)):
                    stack.pop()
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')