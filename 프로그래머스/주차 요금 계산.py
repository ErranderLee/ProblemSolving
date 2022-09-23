import collections
import math


def convert_time(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)


def solution(fees, records):
    answer = []
    num_record = collections.defaultdict(list)

    for record in records:
        time, num, in_or_out = record.split(' ')
        num_record[num].append(convert_time(time))
    car_numbers = list(num_record.keys())
    car_numbers.sort()
    for num in car_numbers:
        if len(num_record[num]) % 2 != 0:
            num_record[num].append(convert_time('23:59'))
        total = 0
        while num_record[num]:
            total += num_record[num].pop() - num_record[num].pop()
        if total < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((total - fees[0]) / fees[2]) * fees[3])

    return answer