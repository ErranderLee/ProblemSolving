import sys

n = int(input())
words = []
for i in range(n):
    words.append(sys.stdin.readline().rstrip())
words.sort(key=lambda x:len(x), reverse=True)

print(words)