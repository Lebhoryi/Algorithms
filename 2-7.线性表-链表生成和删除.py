# coding=utf-8
'''
@ Summary: 整表生成和删除
@ Update:  

@ file:    2-7.线性表-链表生成和删除.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-25 下午10:12
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Link(object):

    @staticmethod
    def c_link(vals):
        if not vals:
            return None
        head = Node(len(vals))
        move = head
        for val in vals:
            tmp = Node(val)
            # 头插法,新元素永远插在第一个节点,头结点之后
            # move2 = head.next
            # head.next = tmp
            # tmp.next = move2
            # 尾插法,新元素永远插在最后一个节点
            move.next = tmp
            move = tmp
        return head, len(vals)

    @staticmethod
    def p_link(link):
        if not link:
            return None
        link = link.next
        while link:
            print(link.val, end=" ")
            link = link.next
        print()

    @staticmethod
    def d_link(link):
        if not link:
            return None
        link.next = None
        return link


if __name__ == "__main__":
    link_a = [1, 2, 1, 4, 3]
    link_a, l_link = Link.c_link(link_a)
    Link.p_link(link_a)
    # Link.p_link(Link.d_link(link_a))


