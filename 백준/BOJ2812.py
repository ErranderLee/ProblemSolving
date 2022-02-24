import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
answer = []

for item in arr:
    while True:
