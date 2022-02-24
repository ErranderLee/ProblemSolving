import sys

n, k = list(map(int, input().split()))
K = k
number = sys.stdin.readline().rstrip()
stack = []

for num in number:
    while k > 0 and stack and stack[-1] < num:
        stack.pop()
        k -= 1
    stack.append(num)

print("".join(stack[:n-K]))