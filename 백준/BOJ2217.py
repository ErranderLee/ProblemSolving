n = int(input())
arr = list()
max_weight = 0

for i in range(n):
    arr.append(int(input()))

for i in range(len(arr)-1, -1, -1):
    temp = arr[i] * (len(arr) - i)
    max_weight = max(temp, max_weight)
print(max_weight)