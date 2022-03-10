import sys
import copy
read = sys.stdin.readline

n = int(read())
arr = []
arr.extend(list(map(int, read().rstrip().split())))
temp = copy.deepcopy(arr)
arr = set(arr)
arr = list(arr)
arr.sort()
dict = {}
for i in range(len(arr)):
    dict[arr[i]] = i
for item in temp:
    print(dict[item], end=' ')
