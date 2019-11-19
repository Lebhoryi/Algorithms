# coding=utf-8
'''
@ Summary: 102.二叉树的层次遍历
@ Update:  https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

@ file:    4-6.二叉树的层序遍历.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-11-19 下午3:39
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

    def list2Node(self, input):
        inputValue = []
        if not input:  return inputValue
        for item in input:
            if item == "null":
                inputValue.append(Node(item))
            else:
                inputValue.append(Node(int(item)))
        if not self.root:
            self.root = inputValue[0]
        queue = [self.root]
        front, index = 0, 1
        while index < len(inputValue):
            node = inputValue[front]
            front += 1

            # left child
            item = inputValue[index]
            index += 1
            if item.val != "null":
                node.left = item
                queue.append(node.left)

            if index >= len(inputValue):  break

            # right child
            item = inputValue[index]
            index += 1
            if item.val != "null":
                node.right = item
                queue.append(node.right)
        return self.root


    def leverOrder(self, root):
        ret = []
        if not root:  return ret
        def helper(node, level):
            # start the current level
            if len(ret) == level:
                ret.append([])

            # append the current node value
            ret[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return ret


    def p_tree(self, root):
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
    _input = list(sys.stdin.readline().strip().split())
    tree = BinTree()
    root = tree.list2Node(_input)
    tree.p_tree(root)
    print(tree.leverOrder(root))
