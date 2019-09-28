# coding=utf-8
'''
@ Summary: 循环链表A之后接循环链表B，成为大的循环链表AB
@ Update:  

@ file:    2-13.链表相接.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-28 下午4:02
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LCLink(object):
    @ staticmethod
    def c_link(vals):
        # Create link
        if not vals:
            return None
        head = Node(len(vals)) # 头指针
        move = head  # 移动指针
        for i in range(len(vals)):
            tmp = Node(vals[i])
            tmp.next = tmp if i == 0 else move.next
            move.next = tmp
            move = tmp
        # rear = Node(len(vals))  # 尾指针
        # rear.next = move
        return move  # 返回最后一个节点

    @ staticmethod
    def p_link(link):
        # Print link
        if not link:
            return None
        cur = link.next
        while cur.next != link.next:
            yield cur.val
            cur = cur.next
        yield cur.val

def merge_link(link_a, link_b):
    # 合并链表AB
    if not link_a and link_b:
        return link_b
    elif link_a and not link_b:
        return link_a
    elif not link_a and not link_b:
        return None
    link_a.next, link_b.next = link_b.next, link_a.next
    return link_b

if __name__ == "__main__":
    # list_ab = []
    list_a = list(range(1, 6))
    list_b = list(range(1, 5))
    # list_ab = list_a + list_b
    link_a = LCLink.c_link(list_a)
    link_b = LCLink.c_link(list_b)

    print("Link A:", end=" ")
    for node in LCLink.p_link(link_a):
        print(node, end=" ")
    print()
    print("Link B:", end=" ")
    for node in LCLink.p_link(link_b):
        print(node, end=" ")
    print()

    link_ab = merge_link(link_a, link_b)
    print("Link AB:", end=" ")
    for node in LCLink.p_link(link_ab):
        print(node, end=" ")
    print()


