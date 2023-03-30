def rotate(key):
  new_key = []
  key = zip(*key)
  for row in key:
    list_key = list(row)
    list_key.reverse()
    new_key.append(list_key)
  return new_key


def get_hole_count(lock):
  count = 0
  for i in range(len(lock)):
    for j in range(len(lock)):
      if lock[i][j] == 0:
        count += 1
  return count


def set_lock(ground, lock, key_length):
  start = (key_length - 1, key_length - 1)
  lock_length = len(lock)
  for i in range(lock_length):
    for j in range(lock_length):
      ground[start[0] + i][start[1] + j] = lock[i][j]

def check(start, ground, key, hole_count):
  key_length = len(key)
  in_count = 0
  for i in range(key_length):
    for j in range(key_length):
      if ground[start[0] + i][start[1] + j] == -1:
        continue
      else:
        if ground[start[0] + i][start[1] + j] == 1 and key[i][j] == 1:
          return False
      if ground[start[0] + i][start[1] + j] == 0 and key[i][j] == 1:
        in_count += 1
      if in_count == hole_count:
        return True
  return False


def solution(key, lock):
  ground_length = 2 * (len(key) - 1) + len(lock)
  ground = [[-1 for i in range(ground_length)] for j in range(ground_length)]
  set_lock(ground, lock, len(key))
  hole_count = get_hole_count(lock)
  for direction in range(4):
    key = rotate(key)
    for i in range(len(lock) + len(key) - 1):
      for j in range(len(lock) + len(key) - 1):
        if check((i, j), ground, key, hole_count):
          return True

  return False