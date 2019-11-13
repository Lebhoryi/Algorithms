# coding=utf-8
'''
@ Summary: 力扣889 给定前序和后序，层序遍历输出
@ http:    https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

@ file:    4-3.给定前序和后序构造二叉树.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-11-9 下午3:52
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)

class Tree(object):
    @ staticmethod
    def constructFromPrePost(pre, post):
        """给定前序和后序构造二叉树

        :param pre: 前序遍历 根-左-右 list
        :param post: 后序遍历 左-右-根 list
        :return: 中序遍历 左-根-右 list
        """
        if not pre :  return
        root = Node(pre[0])
        if len(pre)==1:  return root

        L = post.index(pre[1]) + 1
        root.left = Tree.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = Tree.constructFromPrePost(pre[L+1:], post[L:-1])
        return root


def treeNodeToString(root):
    """ 层序遍历打印二叉树 """
    if not root:  return "[]"
    res = []
    queue = [root]
    while queue:
        cur_node = queue.pop(0)
        res.append(cur_node.val)
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return res

if __name__=="__main__":
    pre = [1,2,4,5,3,6,7]
    post = [4,5,2,6,7,3,1]
    tree = Tree()
    res = treeNodeToString(tree.constructFromPrePost(pre, post))
    print(res)
