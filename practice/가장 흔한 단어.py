import re
import collections


def most_common_word(paragraph, banned):
    words = [word for word in re.sub('[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_common_word(paragraph, banned))