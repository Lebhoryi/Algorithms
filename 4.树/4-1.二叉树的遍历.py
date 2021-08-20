# coding=utf-8
'''
@ Summary: 递归遍历二叉树
@ Update:  

@ file:    4-1.二叉树的遍历.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-11-1 下午7:51
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

    @pysnooper.snoop()
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
            cur_node = queue.pop(0)
            # 左节点不存在时，将elem 作为左节点，否则左节点入队
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            # 右节点不存在时，将elem 作为右节点，否则右节点入队
            if not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


    def layer_order(self):
        """打印层序遍历"""
        if not self.root:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    def pre_order(self, subtree):
        """前序遍历"""
        if not subtree:
            return
        print(subtree)
        self.pre_order(subtree.left)
        self.pre_order(subtree.right)

    def mid_order(self, subtree):
        """中序遍历"""
        if not subtree:
            return
        self.mid_order(subtree.left)
        print(node)
        self.mid_order(subtree.right)

    def post_order(self, subtree):
        """后序遍历"""
        if not subtree:
            return
        self.post_order(subtree.left)
        self.post_order(subtree.right)
        print(subtree)

if __name__=="__main__":
    tree = BinTree()
    for i in range(65,72):
        tree.add(chr(i))
    # tree.layer_order()
    # tree.pre_order(tree.root)
    # tree.mid_order(tree.root)
    tree.post_order(tree.root)
