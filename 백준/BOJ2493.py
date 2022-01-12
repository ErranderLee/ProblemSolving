n = int(input())
stack = []
towers = list(map(int, input().split()))

for i, item in enumerate(towers):
    while len(stack) > 0:
        if item > stack[len(stack) - 1][1]:
            stack.pop()
        else:
            print(stack[len(stack) - 1][0], end=' ')
            break
    if len(stack) == 0:
        print(0, end=' ')
    stack.append([i+1, item])



