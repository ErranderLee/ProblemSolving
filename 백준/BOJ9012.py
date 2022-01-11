n = input()
n = int(n)
arr = []
stack = []
ans = []
for i in range(0, n):
    temp = input()
    arr.append(temp)

for str in arr:
    stack.clear()
    flag = 0
    for ch in str:
        if ch=='(':
            stack.append('(')
        else:
            if len(stack) == 0:
                ans.append('NO')
                flag = 1
                break
            stack.pop()
    if flag == 0:
        if len(stack) > 0:
            ans.append('NO')
        else:
            ans.append('YES')

for answer in ans:
    print(answer)

