def solution(numbers):
  length = len(numbers)
  answer = [-1] * length
  stack = []

  for i, number in enumerate(numbers):
    while stack:
      if stack[-1][1] < number:
        index_pop, index_number = stack.pop()
        answer[index_pop] = number
      else:
        break
    stack.append((i, number))

  return answer