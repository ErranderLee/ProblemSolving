

def str_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return 3600 * h + 60 * m + s


def sec_to_str(time):
    h = time // 3600
    m = (time - h * 3600) // 60
    s = time % 60
    h = ('0'+str(h))[-2:]
    m = ('0'+str(m))[-2:]
    s = ('0'+str(s))[-2:]
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    answer = -1
    times = [0 for _ in range(str_to_sec(play_time)+1)]
    for log in logs:
        start, end = log.split('-')
        times[str_to_sec(start)] += 1
        times[str_to_sec(end)] -= 1

    for i in range(1, len(times)):
        times[i] = times[i] + times[i - 1]
    for i in range(1, len(times)):
        times[i] = times[i] + times[i - 1]

    adv_sec = str_to_sec(adv_time)
    max_temp = -1
    temp_sum = -1
    for i in range(adv_sec - 1, len(times)):
        if i == adv_sec - 1:
            max_temp = times[i]
            answer = i - (adv_sec-1)
        else:
            temp_sum = times[i] - times[i - adv_sec]
            if max_temp < temp_sum:
                max_temp = temp_sum
                answer = i - (adv_sec-1)
    answer = sec_to_str(answer)
    return answer