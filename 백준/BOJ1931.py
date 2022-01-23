n = int(input())
arr = []
count = 0
end = 0
for i in range(0, n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

for item in arr:
    if item[0] >= end:
        end = item[1]
        count += 1
print(count)


