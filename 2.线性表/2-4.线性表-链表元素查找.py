# coding=utf-8
'''
@ Summary: 链表元素查找
@ Update:  

@ file:    2-4.线性表-链表元素查找.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-24 下午6:39
'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Link(object):
    ''' 创建链表 '''
    @staticmethod
    def c_link(vals):
        if not vals:
            return None
        head = ListNode(len(vals))  # 头结点储存的是链表的长度
        move = head
        for val in vals:
            tmp = ListNode(val)
            move.next = tmp
            move = tmp
        return head.next

    @staticmethod
    def p_link(link):
        if not link:
            return None
        while link:
            # print(link.val, end=" ")
            yield link.val
            link = link.next
        # print()

    @staticmethod
    def l_link(link):
        if not link:
            return None
        count = 0
        while link:
            count += 1
            link = link.next
        return count

# 查找链表元素
def get_elem(ln, i, l_link):
    if not ln.next or i < 0 or i > l_link:  # 判断是否是空表,或者i<0
        return None
    cur, count = ln, 1
    while count < i:
        count += 1
        # print(cur.val, end=" ")  # 打印链表
        cur = cur.next  # 指向下一个节点
    return cur.val



if __name__ == "__main__":
    list_a = [1, 2, 3, 4]
    link_a = Link.c_link(list_a)
    l_link = Link.l_link(link_a)
    # for val in Link.p_link(link_a):
    #     print(val, end= " ")
    # print()
    i = 1
    a = get_elem(link_a, i, l_link)
    print(a)
