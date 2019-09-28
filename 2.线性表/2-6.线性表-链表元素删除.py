# coding=utf-8
'''
@ Summary: 单链表中删除元素
@ Update:  

@ file:    2-6.线性表-链表元素删除.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-25 下午8:59
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):   # 这个函数将内容‘友好’地显示出来，否则会显示对象的内存地址
        return str(self.val)

class Link(object):
    @staticmethod
    def create_link(vals):
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

    @staticmethod
    def l_link(link):
        if not link:
            return None
        count = 0
        while link:
            count += 1
            link = link.next
        return count


def del_link(ln, i, lenth_link):
    if not ln or i < 0 or i > lenth_link:
        return None
    cur = ln
    count = 1
    # 找打要删除的节点的上一个节点，pre.next = pre.next.next
    while count < i-1:
        cur = cur.next
        count += 1
    # print(cur.val)
    cur.next = cur.next.next
    return ln



if __name__ == "__main__":
    link_a = [1, 3, 4, 5, 2]
    link_a = Link.create_link(link_a)
    lenth_link = Link.l_link(link_a)
    # Link.p_link(link_a)
    i = 3  # 删除第二个节点
    link_a = del_link(link_a, i, lenth_link)
    for val in Link.p_link(link_a):
        print(val, end=" ")



