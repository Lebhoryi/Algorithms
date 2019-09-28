# coding=utf-8
'''
@ Summary: 有1-n个人，每个人手中随机的正数密码m，第一个m作为上限，从第一个开始数，
           第m个剔除，接着第m个人的密码作为上限，从第m+1个人开始数，最后剩一个人结束
@ Update:  

@ file:    2-12.约瑟夫问题（困难级）.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-28 下午2:53
'''
import random

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LCLink(object):
    @ staticmethod
    def c_link(vals):
        '''Create link

        :param vals: list
        :return rear: the rear node,尾节点,Node
        '''
        if not vals:
            return None
        head = Node(len(vals))  # 头结点，包含数据域，指针域
        move = head  # 移动节点，创建链表使用
        for i in range(len(vals)):
            tmp = Node(vals[i+1])
            tmp.next = tmp if i == 0 else move.next
            move.next = tmp
            move = tmp
        return move  # 返回尾节点，循环链表的强大之处

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

    @ staticmethod
    def l_link(link):
        # The lenth of link
        if not link:
            return 0
        count = 0
        cur = link.next
        while cur.next != link.next:
            cur = cur.next
            count += 1
        return count

    @ staticmethod
    def del_node(link, s, l_link):
        # Delete node
        if not link or s <= 0:
            return None
        s = s%lenth_link if s > l_link else s
        count, cur = 0, link
        if s != 1:
            while count < s-1:
                # 找到要删除的节点的前一个节点
                cur = cur.next
                count += 1
        # 删除操作
        del_node = cur.next
        cur.next = cur.next.next
        return del_node, cur


def joseph(link, s, l_link):
    while l_link > 1:
        # 删除节点
        d_node, link = LCLink.del_node(link, s, l_link)
        print("The deleted node:{}.".format(d_node))
        # print("The link after a node deleted:", end=" ")
        # for node in LCLink.p_link(link):
        #     print(node, end=" ")
        # print()
        # print("The lenth of link: {}.".format(l_link))
        s = d_node.val
        l_link = LCLink.l_link(link)
        print("="*30)
    return link


if __name__ == "__main__":
    _dict = {}
    n, m = 9, 4
    for i in range(1, n):
        _dict[i] = random.randint(1, m)

    # 创建链表
    link = LCLink.c_link(_dict)

    # 打印链表
    print("The origin link:", end=" ")
    for node in LCLink.p_link(link):
        print(node, end=" ")
    print()

    # 链表长度
    lenth_link = LCLink.l_link(link)
    # print("The lenth of link: {}.".format(lenth_link))

    # # 删除节点
    # d_node, link = LCLink.del_node(link, 3, lenth_link)
    # print("The deleted node:{}".format(d_node))
    # print("The link after a node deleted:", end=" ")
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("=" * 30)

    # 加强版的约瑟夫问题
    s = link.next.val  # 第一个节点的数据域的值
    last_node = joseph(link, s, lenth_link)
    print("The last living node: {}.".format(last_node.val))




