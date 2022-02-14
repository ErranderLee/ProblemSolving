n = list(map(int, list(input())))
answer = ''

if 0 not in n:
    print(-1)
else:
    if sum(n) % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        for i in range(len(n)):
            answer += str(n[i])
        print(answer)
