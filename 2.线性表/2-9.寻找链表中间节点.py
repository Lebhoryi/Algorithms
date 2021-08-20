# coding=utf-8
'''
@ Summary: 快速找到未知长度单链表的中间节点
@ Update:  

@ file:    2-9.寻找链表中间节点.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-26 下午6:49
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
            move.next = tmp
            move = tmp
        return head.next

    @staticmethod
    def p_link(link):
        if not link:
            return None
        while link:
            yield link.val
            link = link.next
        print()


def find_mid_node(link):
    cur = link
    cur2 = link.next
    while cur2 and cur2.next:
        cur = cur.next
        cur2 = cur2.next.next

    return cur.val


if __name__ == "__main__":
    list_a = [1, 4, 2, 5, 3, 2, 2]
    link_a = Link.c_link(list_a)
    for val in Link.p_link(link_a):
        print(val, end=" ")
    result = find_mid_node(link_a)
    print(result)
