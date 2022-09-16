import sys
import collections

input = sys.stdin.readline


def rotate(arr):
    arr.appendleft(arr.pop())


def check(count, stage, k):
    if count >= k:
        print(stage)
        sys.exit(0)


n, k = list(map(int, input().rstrip().split()))
durabilities = collections.deque(list(map(int, input().rstrip().split())))
belt = collections.deque([False for _ in range(2*n)])
count = 0
stage = 0
while True:
    stage += 1
    rotate(durabilities)
    rotate(belt)
    if belt[n - 1]:
        belt[n - 1] = False
    for i in range(n-2, -1, -1):
        if belt[i] == True and belt[i + 1] == False and durabilities[i + 1] > 0:
            belt[i] = False
            belt[i + 1] = True
            durabilities[i + 1] -= 1
            if durabilities[i + 1] == 0:
                count += 1
                check(count, stage, k)
        if belt[n - 1]:
            belt[n - 1] = False
    if durabilities[0] > 0 and belt[0] == False:
        belt[0] = True
        durabilities[0] -= 1
        if durabilities[0] == 0:
            count += 1
            check(count, stage, k)
