# coding=utf-8
'''
@ Summary: 用链表实现栈的相关操作
@ Update:  

@ file:    3-2.栈的链接表实现.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-7 下午6:29
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LStack(object):
    @ staticmethod
    def c_link(vals):
        # create link
        if not vals:
            return None
        head = Node(len(vals))  # head node
        move = head  # move node
        for val in vals:
            tmp = Node(val)
            move.next = tmp
            move = tmp
        return head.next

    @ staticmethod
    def p_link(link):
        # print link
        if not link:
            return None
        while link:
            yield link.val
            link = link.next

    @ staticmethod
    def top(link):
        # 取出栈顶元素
        if not link:
            return None
        return link.val

    @ staticmethod
    def push(link, elem):
        # 入栈
        elem = Node(elem)
        elem.next = link
        return elem

    @ staticmethod
    def pop(link):
        # 出栈
        if not link:
            return None
        p = link
        link = link.next
        return p.val, link


if __name__ == "__main__":
    _list = list(range(1, 7))
    # link = None
    # for i in _list:
    #     link = LStack.push(link, i)
    # for node in LStack.p_link(link):
    #     print(node, end=" ")

    top = LStack.c_link(_list)
    for node in LStack.p_link(top):
        print(node, end=" ")
    print()
    # output: 1 2 3 4 5 6

    top = LStack.push(top, 10)
    for node in LStack.p_link(top):
        print(node, end=" ")
    print()
    # output: 10 1 2 3 4 5 6

    elem, top = LStack.pop(top)
    print(elem)
    for node in LStack.p_link(top):
        print(node, end=" ")
    print()

    elem = LStack.top(top)
    print(elem)

