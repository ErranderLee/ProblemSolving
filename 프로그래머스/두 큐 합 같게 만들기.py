from collections import deque


def solution(queue1, queue2):
  answer = 0
  queue1 = deque(queue1)
  queue2 = deque(queue2)
  sum1 = sum(queue1)
  sum2 = sum(queue2)
  len1 = len(queue1)
  len2 = len(queue2)

  while (True):
    if answer > 2 * (len1 + len2):
      return -1

    if sum1 == sum2:
      return answer

    if sum1 > sum2:
      popped = queue1.popleft()
      queue2.append(popped)
      sum1 -= popped
      sum2 += popped
    else:
      popped = queue2.popleft()
      queue1.append(popped)
      sum2 -= popped
      sum1 += popped
    answer += 1
