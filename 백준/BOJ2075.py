import sys

input = sys.stdin.readline
dict = {}

while True:
    tree = input().strip()
    if not tree:
        break
    if tree in dict.keys():
        dict[tree] += 1
    else:
        dict[tree] = 1
total = 0
for value in dict.values():
    total += value
trees = list(dict.keys())
trees.sort()
for tree in trees:
    print('{} {:.4f}'.format(tree, 100*dict[tree]/total))