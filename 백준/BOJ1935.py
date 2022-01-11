n = input()
n = int(n)
s = input()
stack = []
dict = {}
for i in range(0, n):
    dict[chr(65+i)] = int(input())

for i in range(0, len(s)):
    if s[i] == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif s[i] == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif s[i] == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif s[i] == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    else:
        stack.append(dict[s[i]])

ans = stack.pop()
print('{:.2f}'.format(ans))