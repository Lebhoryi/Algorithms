# coding=utf-8
'''
@ Summary: 单链表的元素插入
@ Update:  

@ file:    2-5.线性表-链表元素插入.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-25 下午6:45
'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Link(object):

    @staticmethod
    def c_link(vals):
        # creat link
        if not vals:
            return None
        head = ListNode(len(vals))
        move = head
        for val in vals:
            tmp = ListNode(val)
            move.next = tmp
            move = tmp
        return head.next

    @staticmethod
    def p_link(ln):
        # print link
        if not ln:
            return None
        while ln:
            print(ln.val, end=" ")
            ln = ln.next
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


def insert_elem(ln, node, s, lenth_link):
    """单链表中插入元素

    :param ln: node
    :param a: node
    :param s: int
    :return: node
    """
    if not ln or s < 0 or s > lenth_link:
        return None
    cur = ln
    count = 1
    while count < s:
        cur = cur.next
        count += 1

    node = ListNode(node)
    node.next = cur.next
    cur.next = node
    return ln


if __name__ == "__main__":
    link_a = [1, 2, 3, 4]
    node_b, s = 5, 2  # 在第二个节点的位置插入5

    link_a = Link.c_link(link_a)
    lenth_link = Link.l_link(link_a)
    Link.p_link(link_a)

    link_b = insert_elem(link_a, node_b, s, lenth_link)
    Link.p_link(link_b)
