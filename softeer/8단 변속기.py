import sys

def solution(numbers):
  isAccending = False
  isDescending = False
  for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
      isAccending = True
    else:
      isDescending = True

    if isAccending and isDescending:
      return "mixed"
  if isAccending:
    return "ascending"
  return "descending"

read = sys.stdin.readline
numbers = list(map(int, read().rstrip().split(' ')))

print(solution(numbers))