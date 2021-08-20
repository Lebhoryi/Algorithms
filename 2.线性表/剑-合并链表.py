# coding=utf-8
'''
@ Summary: 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
@ Update:  

@ file:    剑-合并链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-1 上午11:58
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

def merge(pHead1, pHead2):
    # 自己的
    if not pHead1 and pHead2:
        return None
    elif not pHead2:
        return pHead1
    elif not pHead1:
        return pHead2
    result = []
    while pHead1:
        result.append(pHead1.val)
        pHead1 = pHead1.next
    while pHead2:
        result.append(pHead2.val)
        pHead2 = pHead2.next
    result = sorted(result)
    head = Node(len(result))
    move = head
    for val in result:
        tmp = Node(val)
        move.next = tmp
        move = tmp
    return head.next

def merge2(pHead1, pHead2):
    # 牛客榜首
    if not pHead1 and pHead2:
        return None
    head = Node(0)
    move = head
    while pHead1 and pHead2:
        if pHead1.val <= pHead2.val:
            move.next = pHead1
            pHead1 = pHead1.next
        else:
            move.next = pHead2
            pHead2 = pHead2.next
        move = move.next
    move.next = pHead1 or pHead2
    return head.next


if __name__ == "__main__":
    _list = [1, 2, 3]
    _list2 = [2 ,3 ,4]
    link = Link.c_link(_list)
    link2 = Link.c_link(_list2)
    # for node in Link.p_link(link):
    #     print(node, end=" ")
    # print()
    link = merge2(link, link2)
    for node in Link.p_link(link):
        print(node, end=" ")
    print()
