n = int(input())
arr = list(map(int, input().split()))
sum = 0
result = 0
arr.sort()
for item in arr:
    sum = sum + item
    result += sum
print(result)