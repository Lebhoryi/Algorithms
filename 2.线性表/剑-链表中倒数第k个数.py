# coding=utf-8
'''
@ Summary: 链表中倒数第k个数
@ Update:  

@ file:    剑-链表中倒数第k个数.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-1 上午10:37
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
        # creat link
        if not vals:
            return None
        head = Node(len(vals))  # head node
        move = head
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


def find_node(head, k):
    # 输入一个链表，输出该链表中倒数第k个结点
    if not head:
        return None
    result = []
    while head:
        result.append(head)
        head = head.next
    return result[-k] if k > 0 and k <= len(result) else None

if __name__ == "__main__":
    a = list(range(6))
    link = Link.c_link(a)
    # for node in Link.p_link(link):
    #     print(node, end=" ")
    # print()

    print(find_node(link, 5))
