# coding=utf-8
'''
@ Summary: 力扣 236
@ Http:    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

@ file:    4-3.二叉树的最近公共祖先.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-11-15 下午3:09
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)

class Tree(object):
    def __init__(self):
        self.root = None

    def list2Node(self, input):
        # 列表转层序遍历
        if not input:  return []
        inputValues = [Node(item) for item in input]
        if not self.root:
            self.root = inputValues[0]
        queue = [self.root]
        front, index = 0, 1
        while index < len(inputValues):
            # 父节点
            node = inputValues[front]
            front += 1

            # 左节点
            item = inputValues[index]
            index += 1
            if item != "null":
                node.left = item
                queue.append(item)

            if index >=  len(inputValues):  break

            # 右节点
            item = inputValues[index]
            index += 1
            if item != "null":
                node.right = item
                queue.append(item)
        return self.root

    def lowestCommonAncestor(self, root, p, q):
        if root == None or root.val in {p, q}: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


if __name__ == "__main__":
    import sys
    input = list(sys.stdin.readline().strip().split())
    tree = Tree()
    root = tree.list2Node(input)
    # print(type(root.val))
    ret = tree.lowestCommonAncestor(root, str(5), str(4))
    print(ret)