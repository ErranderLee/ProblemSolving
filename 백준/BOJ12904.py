import sys
read = sys.stdin.readline

s = read().rstrip()
t = read().rstrip()

while len(s) != len(t):
    if t[-1] == 'A':
        t = t[:len(t) - 1]
    else:
        t = t[:len(t) - 1]
        t = t[::-1]
if s == t:
    print(1)
else:
    print(0)

