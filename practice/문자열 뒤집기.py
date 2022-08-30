# 리턴 없이 리스트 내부 직접 조작해야함
import datetime


def execute(s, method):
    start = datetime.datetime.now()
    method(s)
    print(s)
    end = datetime.datetime.now()
    print(method.__name__, (end - start).microseconds)


def reverse_string_v1(s) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_v2(s) -> None:
    s.reverse()


if __name__ == '__main__':
    test_list = list('hello')
    execute(test_list, reverse_string_v1)
    execute(test_list, reverse_string_v2)