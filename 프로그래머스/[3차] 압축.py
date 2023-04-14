

def init_index():
  index = dict()
  for i in range(1, 27):
    index[chr(64 + i)] = i
  return index


def find_max(index, msg, start):
  end = start + 1
  result = 0
  while (end <= len(msg)):
    part = msg[start:end]
    if part in index:
      result = index[part]
      end += 1
    else:
      index[part] = len(index) + 1
      end -= 1
      break
  return result, end


def solution(msg):
  answer = []
  index = init_index()
  start = 0
  while (True):
    result, end = find_max(index, msg, start)
    if result == 0:
      break
    answer.append(result)
    start = end
  return answer