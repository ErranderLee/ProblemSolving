

answer = set()


def rec(X, N, have):

    global answer
    if X == 0:
        cand = list(have)
        cand.sort()
        answer.add(tuple(cand))
        return
    elif X < 0:
        return
    until = int(X**(1/N))
    for i in range(until, 0, -1):
        if i not in have:
            temp = X - i ** N
            rec(temp, N, set(list(have) + [i]))
        else:
            break


def powerSum(X, N):
    # Write your code here
    global answer
    rec(X, N, set())
    return len(answer)

print(powerSum(100, 3))
