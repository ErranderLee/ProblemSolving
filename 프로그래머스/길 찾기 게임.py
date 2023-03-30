from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
  answer = []
  indexed_nodeinfo = sort_nodeinfo_with_index(nodeinfo)
  tree_info = defaultdict(list)
  get_tree_info(tree_info, indexed_nodeinfo)
  answer.append(preorder(tree_info, indexed_nodeinfo[0]))
  answer.append(postorder(tree_info, indexed_nodeinfo[0]))

  return answer


def sort_nodeinfo_with_index(nodeinfo):
  indexed_nodeinfo = []
  for i in range(len(nodeinfo)):
    indexed_nodeinfo.append([nodeinfo[i][0], nodeinfo[i][1], i + 1])
  indexed_nodeinfo.sort(key=lambda x : (-x[1], x[0]))

  return indexed_nodeinfo


def get_tree_info(tree_info, indexed_nodeinfo):
  def make_tree_info(nodeinfos):
    left = []
    right = []
    if len(nodeinfos) == 0:
      return
    root = nodeinfos[0]
    root_x = root[0]
    for i in range(1, len(nodeinfos)):
      current_node = nodeinfos[i]
      current_node_x = current_node[0]
      if current_node_x > root_x:
        right.append(current_node)
      else:
        left.append(current_node)
    left_index = None
    right_index = None
    if len(left) != 0:
      left_index = left[0][2]
    if len(right) != 0:
      right_index = right[0][2]
    if left_index == None and right_index == None:
      return
    root_index = root[2]
    tree_info[root_index].append((left_index, right_index))
    make_tree_info(left)
    make_tree_info(right)

  make_tree_info(indexed_nodeinfo)


def preorder(tree_info, root):
  result = []
  root_index = root[2]
  def rec(index):
    if index == None:
      return
    result.append(index)
    if index in tree_info:
      next_node = tree_info[index][0]
      rec(next_node[0])
      rec(next_node[1])
  rec(root_index)

  return result


def postorder(tree_info, root):
  result = []
  root_index = root[2]
  def rec(index):
    if index == None:
      return
    if index in tree_info:
      next_node = tree_info[index][0]
      rec(next_node[0])
      rec(next_node[1])
    result.append(index)
  rec(root_index)

  return result