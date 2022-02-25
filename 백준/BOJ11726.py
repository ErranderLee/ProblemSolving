import collections

n = int(input())
dict = collections.defaultdict(list)
dict[1].append(1)
dict[2].extend([1, 1])

def solution(n):
    for i in range(3, n + 1):
        dict[i].extend([1, i-1])
        for j in range(1, int(i/2)):
            if i % 2 == 0 and j == int(i/2) - 1:
                dict[i].append(1)
            else:
                dict[i].append(dict[i-1][j+1] + dict[i-2][j])
solution(n)
print(sum(dict[n])%10007)
