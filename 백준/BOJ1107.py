import sys
read = sys.stdin.readline

target = read().rstrip()
n = int(read())
malfunctioned = []
malfunctioned.extend(list(map(int, read().rstrip().split())))
functioned = []
for i in range(10):
    if i not in malfunctioned:
        functioned.append(i)
functioned.sort()
minValue = 500000

if int(target) == 100:
    print(0)
    sys.exit(0)
else:
    minValue = min(minValue, abs(int(target)-100))

for i in range(1000000):
    for j in range(len(str(i))):
        if int(str(i)[j]) not in functioned:
            break
        if j == len(str(i)) - 1:
            minValue = min(minValue, abs(int(target) - i) + len(str(i)))
print(minValue)