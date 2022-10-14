import collections


def isValid(s):
    # Write your code here
    count_ch = collections.Counter(s)
    if len(set(count_ch.values())) == 1:
        return "YES"
    elif len(set(count_ch.values())) > 2:
        return "NO"
    else:
        for ch in count_ch:
            count_ch[ch] -= 1
            temp = set(count_ch.values())
            if 0 in temp:
                temp.remove(0)
            if len(temp) == 1:
                return "YES"
            else:
                count_ch[ch] += 1
        return "NO"


print(isValid('aabbc'))