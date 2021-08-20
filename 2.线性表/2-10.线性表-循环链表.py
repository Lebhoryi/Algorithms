# coding=utf-8
'''
@ Summary: 循环链表及操作
@ Update:  

@ file:    2-10.线性表-循环链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-26 下午7:45
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):   # 这个函数将内容‘友好’地显示出来，否则会显示对象的内存地址
        return str(self.val)


class CLink(object):
    @ staticmethod
    def c_link(vals):
        # 创建循环链表
        if not vals:
            return None
        # 创建头结点
        head = Node(len(vals))
        move = head
        # 考虑到第一个节点先形成循环链表的情况
        # 然后是新的节点指向等同于移动节点的指向
        for i in range(len(vals)):
            tmp = Node(vals[i])
            tmp.next = tmp if i == 0 else move.next
            move.next = tmp
            move = tmp
        # return head
        # 循环链表用尾节点比头结点友好，据说
        rear = head
        rear.next = move
        return rear

    @ staticmethod
    def p_link(link):
        # 打印循环链表
        if not link:
            return None
        cur = link.next.next  # cur为第一个节点，接着为当前节点
        while cur.next != link.next.next:
            # print(cur, link.next)
            yield cur.val
            cur = cur.next
        yield cur.val
        print()

    @ staticmethod
    def l_link(link):
        # lenth of link
        if not link:
            return None
        cur, count = link.next.next, 1
        # 判断条件是最后一个指向是否是第一个节点
        while cur.next != link.next.next:
            count += 1
            cur = cur.next
        return count

    @ staticmethod
    def add_node(link, node, s, l_link):
        if not link or not node or s < 0:
            return None
        s = s % l_link if s > l_link else s
        node = Node(node)
        cur = link.next.next
        if s == l_link:
            # cur指向第一个节点，最后一个节点指向cur
            node.next = cur
            link.next.next = node
        else:
            count = 1
            while count < s:
                # 找到要插入的cur位置
                cur = cur.next
                count += 1
            # cur指向下一个节点，当前节点指向cur
            node.next = cur.next
            cur.next = node
        return link

    @ staticmethod
    def del_node(link, s, l_link):
        if not link or s < 0:
            return None
            # 存在s>l_link的情况，需要对s做一步处理
        s = s % l_link if s > l_link else s
        cur = link.next.next
        count = 1
        while count < s:
            cur = cur.next
            count += 1
        # 当前cur指向下下一个节点，跳过下一个节点
        cur.next = cur.next.next
        return link

    @ staticmethod
    def find_node(link, s, l_link):
        if not link or s < 0:
            return None
        s = s % l_link if s > l_link else s
        cur = link.next.next
        count = 1
        while count < s:
            cur = cur.next
            count += 1
        return cur.val


if __name__ == "__main__":
    list_a = [1, 2, 1, 5, 3, 7]
    link_a = CLink.c_link(list_a)
    [print(node, end=" ") for node in CLink.p_link(link_a)]

    # 插入节点，在尾部插入节点的复杂度为O(1)
    lenth_link = CLink.l_link(link_a)
    node, s = 666, 10
    link_a = CLink.add_node(link_a, node, s, lenth_link)
    [print(node, end=" ") for node in CLink.p_link(link_a)]


    # delete node
    link_a = CLink.del_node(link_a, s, lenth_link)
    [print(node, end=" ") for node in CLink.p_link(link_a)]

    # find node
    node_a = CLink.find_node(link_a, s, lenth_link)
    print(node_a)





