import re
import datetime
import collections


def execute(s, method):
    start = datetime.datetime.now()
    print(method(s))
    end = datetime.datetime.now()
    print(method.__name__, (end - start).microseconds)


def is_palindrome_v1(s: str) -> bool:
    strs = []
    for ch in s:
        if ch.isalnum():
            strs.append(ch.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome_v2(s: str) -> bool:
    strs: collections.deque = collections.deque()

    for ch in s:
        if ch.isalnum():
            strs.append(ch)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def is_palindrome_v3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


if __name__ == '__main__':
    test_str = 'A man, a plan, a canal: Panama'
    execute(test_str, is_palindrome_v1)
    execute(test_str, is_palindrome_v2)
    execute(test_str, is_palindrome_v3)