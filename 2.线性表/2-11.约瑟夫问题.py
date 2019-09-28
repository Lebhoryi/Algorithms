# coding=utf-8
'''
@ Summary: 约瑟夫问题，题目自行百度
@ Update:  存在特殊情况，s=1

@ file:    2-11.约瑟夫问题.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-27 下午5:22
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


class LCLink(object):
    @staticmethod
    def c_link(vals):
        if not vals:
            return None
        head = Node(len(vals))  # 头结点
        move = head     # 移动节点
        # rear = head
        for i in range(len(vals)):
            tmp = Node(vals[i])
            # 考虑到第一个节点先形成循环链表的情况
            # 然后是新的节点指向等同于移动节点的指向
            tmp.next = tmp if i == 0 else move.next
            move.next = tmp
            move = tmp
        # rear.next = move  # 尾节点
        return move

    @staticmethod
    def p_link(link):
        if not link:
            return None
        cur = link.next
        while cur.next != link.next:
            yield cur.val
            cur = cur.next
        yield cur.val

    @staticmethod
    def l_link(link):
        if not link:
            return 0
        cur = link.next
        count = 1
        while cur.next != link.next:
            cur = cur.next
            count += 1
        return count

    @staticmethod
    def del_node(link, s, l_link):
        if not link or s < 0:
            return None
        s = s%l_link if s > l_link else s
        count, cur = 0, link
        if s != 1:
            while count < s-1:
                cur = cur.next
                count += 1
        del_node = cur.next  # 要删除的节点
        cur.next = cur.next.next  # 删除节点操作
        # return link  # 这是普通删除节点的return
        return del_node, cur


def joseph(link, s, l_link):
    while l_link > 2:
        del_node, link = LCLink.del_node(link, s, l_link)
        l_link = LCLink.l_link(link)
        print("The '{}' node have deleted.".format(del_node))  # 删除的节点
        # print("The link's first node: {}".format(link_a))  # 指向第一个节点之前的节点
        # print("The lenth of link:{}".format(lenth_link))  # 链表的长度
        # print("="*30)
    return link


if __name__ == "__main__":
    list_a = list(range(1, 9))

    # Creating link
    link_a = LCLink.c_link(list_a)

    # Printing link
    for node in LCLink.p_link(link_a):
        print(node, end=" ")
    print()

    # Lenth of link
    lenth_link = LCLink.l_link(link_a)
    # print(lenth_link)

    # Deleting node
    # s = 1
    # _, link_a = LCLink.del_node(link_a, s, lenth_link)
    # for node in LCLink.p_link(link_a):
    #     print(node, end=" ")
    # print()

    s = 1
    link_a = joseph(link_a, s, lenth_link)

    # Printing the final link
    print("The living node: ", end="")
    for node in LCLink.p_link(link_a):
        print(node, end=" ")
    print()


