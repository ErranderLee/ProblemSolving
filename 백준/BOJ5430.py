import sys
read = sys.stdin.readline

t = int(read())
answers = []
for i in range(t):
    funcs = read().rstrip()
    n = int(read().rstrip())
    arr = read().rstrip()
    arr = arr[1:len(arr)-1].split(',')
    if arr[0] != '':
        arr = list(map(int, arr))
    countsToRemove = [0, 0]
    rev = False
    for ch in funcs:
        if ch == 'R':
            rev = not rev
        else:
            if rev:
                countsToRemove[1] += 1
            else:
                countsToRemove[0] += 1
    if sum(countsToRemove) > n:
        answers.append('error')
    else:
        if rev:
            temp = arr[countsToRemove[0]:n-countsToRemove[1]]
            answers.append(temp[::-1])
        else:
            answers.append(arr[countsToRemove[0]:n - countsToRemove[1]])
for answer in answers:
    if answer != 'error' and len(answer) > 1:
        for i in range(len(answer)):
            if i == 0:
                print('[', end='')
                print(answer[i], end='')
                print(',', end='')
            elif i == len(answer) - 1:
                print(answer[i], end='')
                print(']')
            else:
                print(answer[i], end='')
                print(',', end='')
    else:
        print(answer)