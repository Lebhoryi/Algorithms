# coding=utf-8
'''
@ Summary: 左右子树反转
@ Update:  

@ file:    4-2.左右反转二叉树.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-11-9 下午3:46
'''
import pysnooper

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class BinTree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    # @pysnooper.snoop(watch="queue")
    def add(self, elem):
        '''创建二叉树'''
        node = Node(elem)
        # 如果根节点为空，则elem作为根节点
        if not self.root:
            self.root = node
            return
        # 根节点入队
        queue = [self.root]
        while queue:
            # 父节点出队
            par_node = queue.pop(0)
            # 左节点不存在时，将elem 作为左节点，否则左节点入队
            if not par_node.left:
                par_node.left = node
                return
            else:
                queue.append(par_node.left)
            # 右节点不存在时，将elem 作为右节点，否则右节点入队
            if not par_node.right:
                par_node.right = node
                return
            else:
                queue.append(par_node.right)

    def reverse(self, subtree):
        if not subtree:
            return
        subtree.left, subtree.right = subtree.right, subtree.left
        self.reverse(subtree.left)
        print(subtree)
        self.reverse(subtree.right)

if __name__=="__main__":
    tree = BinTree()
    for i in range(65,72):
        tree.add(chr(i))
    tree.reverse(tree.root)