# coding=utf-8
'''
@ Summary: 输入一个链表，反转链表后，输出新链表的表头。
@ Update:  

@ file:    剑-反转链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-1 上午10:51
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

def reverse_link(pHead):
    # 自己想的
    if not pHead or not pHead.next:
        return pHead
    result, cur, cur2 = [], pHead, pHead
    while cur:
        result.append(cur.val)
        cur = cur.next
    for i in range(1, len(result) + 1):
        cur2.val = result[-i]
        cur2 = cur2.next
    return pHead


def rev_link(pHead):
    # 牛客网榜首
    if not pHead or not pHead.next:
        return pHead
    last = None
    while pHead:
        tmp = pHead.next
        pHead.next = last
        last = pHead
        pHead = tmp
    return last




if __name__ == "__main__":
    a = list(range(6))
    link = Link.c_link(a)
    for node in Link.p_link(link):
        print(node, end=" ")
    print()

    link = rev_link(link)
    for node in Link.p_link(link):
        print(node, end=" ")
    print()
