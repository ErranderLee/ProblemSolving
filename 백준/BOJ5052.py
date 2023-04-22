
def solution(numbers):
  if len(numbers) == 1:
    return 'YES'
  numbers.sort()
  for i in range(len(numbers) - 1):
    cur = numbers[i]
    if cur == numbers[i + 1][:len(cur)]:
        return 'NO'
  return 'YES'


if __name__ == '__main__':
  t = int(input())
  answer = []
  for i in range(t):
    n = int(input())
    numbers = []
    for j in range(n):
      numbers.append(input())
    answer.append(solution(numbers))
  for result in answer:
    print(result)