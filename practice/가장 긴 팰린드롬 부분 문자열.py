

def longest_palindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 and s[:] == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    return result

print(longest_palindrome('121210989372839487123454321784938'))