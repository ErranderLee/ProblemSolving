def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x * 3)
    for item in numbers:
        answer += item

    return str(int(answer))
