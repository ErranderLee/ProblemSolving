import sys

read = sys.stdin.readline

def get_rank(contest):
  index_score = dict()
  sort_arr = []
  for j, score in enumerate(contest):
    sort_arr.append((score, j))
  sort_arr.sort(key=lambda x: x[0], reverse=True)

  rank = 1
  same_count = 1
  index_score[sort_arr[0][1]] = rank
  cur_score = sort_arr[0][0]
  for j in range(1, len(sort_arr)):
    score, index = sort_arr[j]
    if cur_score == score:
      index_score[index] = rank
      same_count += 1
    else:
      rank = rank + same_count
      index_score[index] = rank
      same_count = 1
      cur_score = score

  return index_score


def print_result(n, index_score):
  for i in range(n):
    print(index_score[i], end=' ')
  print()


def solution(n, contests):
  total = [0] * n
  for contest in contests:
    index_score = get_rank(contest)
    print_result(n, index_score)
    for i, score in enumerate(contest):
      total[i] += score


  index_score = get_rank(total)
  print_result(n, index_score)


n = int(read().rstrip())
contests = []
for i in range(3):
  contests.append(list(map(int, read().rstrip().split(' '))))

solution(n, contests)