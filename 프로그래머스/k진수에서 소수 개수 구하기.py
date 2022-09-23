import re
import math


def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True


def convert(n, k):
    res = ''
    while n > 0:
        res += str(n % k)
        n //= k
    return res[::-1]


def get_numbers(converted):
    return list(filter(None, re.split('[0+]', converted)))


def solution(n, k):
    answer = 0
    converted = convert(n, k)
    numbers = get_numbers(converted)
    for number in numbers:
        if is_prime(int(number)):
            answer += 1
    return answer