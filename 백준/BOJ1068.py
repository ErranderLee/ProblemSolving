from collections import defaultdict

n = int(input())
nodes = list(map(int, input().split()))
tree = defaultdict(list)
parent = []
for i, item in enumerate(nodes):
    tree[item].append(i)
    parent.append(item)
global nodeToDelete
nodeToDelete = int(input())

def deleteNode(nodeToDelete):
    if tree[nodeToDelete]:
        for item in tree[nodeToDelete]:
            deleteNode(item)
        del tree[nodeToDelete]

global count
count = 0
def findNumLeafNodes(pos):
    global count
    global nodeToDelete

    if not tree[pos] and pos != -1:
        # print(pos)
        count += 1
    for item in tree[pos]:
        findNumLeafNodes(item)

# print(tree)
deleteNode(nodeToDelete)
# print(tree)
tree[parent[nodeToDelete]].remove(nodeToDelete)
# print(tree)
findNumLeafNodes(-1)
print(count)
