
def convert_minute(time):
  start_hour, start_minute = time[0].split(':')
  end_hour, end_minute = time[1].split(':')

  def convert(hour, minute):
    return int(hour) * 60 + int(minute)

  return [convert(start_hour, start_minute), convert(end_hour, end_minute)]


def solution(book_time):
  answer = 0
  minutes = [0] * (24*60)
  for time in book_time:
    start, end = convert_minute(time)
    minutes[start] += 1
    if end + 10 < 24 * 60:
      minutes[end + 10] -= 1

  for i in range(1, len(minutes)):
    minutes[i] += minutes[i - 1]

  return max(minutes)

# 누적합을 이용하는 문제
# 시작 시간에 1을 더하고 종료 시간 + 1에 -1을 더한다(누적으로 더할 것이기 때문에 종료 시간 + 1은 차지하고 있는 시간이 아니라 1을 빼준다).