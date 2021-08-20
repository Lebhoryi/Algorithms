# coding=utf-8
'''
@ Summary: n*n 的矩阵，矩阵中有n种不同的元素，每种元素有n个，每种元素在一行和一列中
           只出现一次
@ Update:  

@ file:    2-16.拉丁方阵.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-29 下午4:27
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
        # print link
        if not vals:
            return None
        head = Node(len(vals))  # head node
        move = head  # move node
        for i in range(len(vals)):
            tmp = Node(vals[i])
            tmp.next = tmp if i == 0 else move.next
            move.next = tmp
            move = tmp
        return move  # 返回尾节点

    @ staticmethod
    def p_link(link):
        # print link
        if not link:
            return None
        cur = link.next
        while cur.next != link.next:
            yield cur.val
            cur = cur.next
        yield cur.val


    @ staticmethod
    def l_link(link):
        # lenth of link
        if not link:
            return 0
        cur, count = link.next, 1
        while cur.next != link.next:
            cur = cur.next
            count += 1
        return count


def o_link(link):
    # 将首节点变为尾节点
    return link.next

def latin_square(link, l_link):
    count = 0
    while count < l_link:
        # print("The {} line: ".format(i), end="")
        for node in LCLink.p_link(link):
            print(node, end=" ")
        print()
        link = link.next
        count += 1


if __name__ == "__main__":
    _list = list(range(1, 9))
    link = LCLink.c_link(_list)
    for node in LCLink.p_link(link):
        print(node, end=" ")
    print()
    print("="*30)

    lenth_link = LCLink.l_link(link)
    # print(lenth_link)
    latin_square(link, lenth_link)




