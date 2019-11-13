# coding=utf-8
'''
@ Summary: 力扣98
@ Http:    https://leetcode-cn.com/problems/validate-binary-search-tree/

@ file:    4-4.验证搜索二叉树.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-11-10 下午1:21
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)

class BinTree(object):
    def __init__(self):
        self.root = None

    def isValidBST(self, root):
        # 中序遍历 递归 不推荐
        def in_order(root):
            if not root:  return []
            return in_order(root.left) + [root.val] + \
                   in_order(root.right)
        in_order = in_order(root)
        return in_order == list(sorted(set(in_order)))

    def isValidBST2(self, root):
        # 最大值 最小值
        def helper(node, minval=-float("inf"), maxval=float("inf")):
            if not node:  return True
            if not minval < int(node.val) < maxval:  return False
            return helper(node.left, minval, int(node.val)) and \
                   helper(node.right, int(node.val), maxval)
        return helper(root)


    def string2node(self, input):
        if not input: return []
        inputValue = [Node(item) for item in input]
        if not self.root:
            self.root = inputValue[0]  # 首节点
        queue = [self.root]  # 首节点入队
        front, index = 0, 1
        while index < len(inputValue):
            node = inputValue[front]
            front += 1

            # 左孩子
            item = inputValue[index]
            index += 1
            if item != "null":
                node.left = item
                queue.append(node.left)

            if index >= len(inputValue):  break

            # 右孩子
            item = inputValue[index]  # 为了跳过null 元素
            index += 1
            if item != "null":
                node.right = item
                queue.append(node.right)


def stringToTreeNode(inputValues):
    """list to 层序遍历"""
    if not inputValues:  return []
    root = Node(inputValues[0])  # 顶点
    queue = [root]  # 顶点入队
    front, index = 0, 1
    while index < len(inputValues):
        node = queue[front]
        front += 1

        item = inputValues[index]
        index += 1
        if item != "null":
            node.left = Node(item)
            queue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index += 1
        if item != "null":
            node.right = Node(item)
            queue.append(node.right)
    return root


def printTree(root):
    """打印层序遍历树"""
    if not root:  return []
    queue = [root]
    while queue:
        cur_node = queue.pop(0)
        print(cur_node, end=" ")
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    print()


if __name__ == "__main__":
    import sys
    lines = list(sys.stdin.readline().strip().split())
    tree = BinTree()
    tree.string2node(lines)
    # printTree(tree.root)
    ret = tree.isValidBST2(tree.root)
    print(ret)

