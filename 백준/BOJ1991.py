n = int(input())
tree = dict()

for i in range(n):
    temp = input().split()
    tree[temp[0]] = []
    for i in range(1, 3):
        tree[temp[0]].append(temp[i])

def preorder(tree, pos):
    print(pos, end='')
    if tree[pos][0] != '.':
        preorder(tree, tree[pos][0])
    if tree[pos][1] != '.':
        preorder(tree, tree[pos][1])

def inorder(tree, pos):
    if tree[pos][0] != '.':
        inorder(tree, tree[pos][0])
    print(pos, end='')
    if tree[pos][1] != '.':
        inorder(tree, tree[pos][1])

def postorder(tree, pos):
    if tree[pos][0] != '.':
        postorder(tree, tree[pos][0])
    if tree[pos][1] != '.':
        postorder(tree, tree[pos][1])
    print(pos, end='')

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
