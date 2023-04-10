from itertools import combinations


def create_candidates(columns):
  candidates = []
  for i in range(1, len(columns) + 1):
    candidates.extend(list(combinations(columns, i)))
  return candidates


def check_if_key(candidate, relation):
  relation_len = len(relation)
  candidate_len = len(candidate)
  value_set = set()
  for i in range(relation_len):
    value = []
    for j in range(candidate_len):
      nth_column = candidate[j] - 1
      value.append(relation[i][nth_column])
    value = tuple(value)
    if value in value_set:
      return False
    else:
      value_set.add(value)
  return True


def remove_from_set(candidates_comp, key):
  to_delete = []
  for candidate in candidates_comp:
    check = True
    for num in key:
      if num not in candidate:
        check = False
    if check:
      to_delete.append(candidate)
  for el in to_delete:
    candidates_comp.remove(el)


def solution(relation):
  answer = 0
  columns = [i for i in range(1, len(relation[0]) + 1)]
  candidates = create_candidates(columns)
  candidates_comp = set(candidates)

  for candidate in candidates:
    if candidate not in candidates_comp:
      continue
    if check_if_key(candidate, relation):
      answer += 1
      remove_from_set(candidates_comp, candidate)

  return answer