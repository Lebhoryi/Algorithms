# coding=utf-8
'''
@ Summary: 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
@ Update:  

@ file:    剑-从尾到头打印链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-30 上午11:46
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class Link(object):
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
        cur = link
        while cur:
            yield cur.val
            cur = cur.next


def p_link_reverse(link):
    # 翻转链表
    result = []
    if not link:
        return None
    while link:
        result.append(link.val)
        link = link.next
    return result[::-1]

def link_reverse(link):
    if not link or link.next:
        return
    last = None
    while link:
        tmp = link.next
        link.next = last
        last = link
        link = tmp
    return last


if __name__ == "__main__":
    _list = [1, 2, 3]
    link = Link.c_link(_list)
    # for node in Link.p_link(link):
    #     print(node, end=" ")
    # print()
    print(p_link_reverse(link))
    link = link_reverse(link)
    for node in Link.p_link(link):
        print(node, end=" ")
    print()

