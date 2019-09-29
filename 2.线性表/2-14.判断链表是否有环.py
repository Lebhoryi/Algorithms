# coding=utf-8
'''
@ Summary: 1 - 2 - 3 - 4 - 2 存在环,用快慢指针
@ Update:

@ file:    2-14.判断链表是否有环.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-28 下午4:29
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
        # 创建单链表
        if not vals:
            return None
        head = Node(len(vals))  # 头结点
        move = head  # 移动节点
        for val in vals:
            tmp = Node(val)
            move.next = tmp
            move = tmp
        return head

    @ staticmethod
    def p_link(link):
        # print link
        if not link:
            return None
        cur = link.next
        while cur:
            yield cur.val
            cur = cur.next

class LCLink(object):
    @ staticmethod
    def c_link(vals, s):
        # 创建单链表
        if not vals or s <= 0 or s > len(vals):
            return None
        head = Node(len(vals))  # 头结点
        move = head  # 移动节点
        for i in range(len(vals)):
            tmp = Node(vals[i])
            tmp.next = tmp if i == s-1 else move.next
            move.next = tmp
            move = tmp
        return head, move

    @ staticmethod
    def p_link(link, rear, s):
        # print link
        if not link:
            return None
        cur = link.next
        count = 1
        while count < s:
            yield cur.val
            count += 1
            cur = cur.next
        while cur.next != rear.next:
            yield cur.val
            cur = cur.next
        yield cur

def is_lclink(link):
    p = q = link
    while p and q and q.next:
        p = p.next
        if q.next:
            q = q.next.next
        print("p: {}  q: {}".format(p, q))
        if p == q:
            return "This link is a cycle link"
    return "This link is not a cycle link"


if __name__ == "__main__":
    list_a = list_b = list(range(1, 7))
    link_a = Link.c_link(list_a)
    s = 2
    link_b, rear_b = LCLink.c_link(list_b, s)
    for node in Link.p_link(link_a):
        print(node, end=" ")
    print()
    for node in LCLink.p_link(link_b, rear_b, s):
        print(node, end=" ")
    print()
    print("=" * 30)
    print(is_lclink(link_b))






