# coding=utf-8
'''
@ Summary: 最上面的牌为1，抽出，接着数两张，第二张是2，抽出，继续操作，直到没有扑克牌为止
@ Update:  

@ file:    2-15.魔术师发牌问题.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-28 下午10:28
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
        head = Node(len(vals))  # head node
        move = head  # moving node
        for i in range(len(vals)):
            tmp = Node(vals[i])
            tmp.next = tmp if i == 0 else move.next
            move.next = tmp
            move = tmp
        return move

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
            return None
        cur, count = link.next, 1
        while cur.next != link.next:
            count += 1
            cur = cur.next
        return count

    @ staticmethod
    def res_link(link, s):
        # 第s+1个节点作为首节点
        if not link:
            return None
        cur, count = link, 0
        while count < s-1 or cur.next.val != 0:  # 找到第s-1个的点或者首节点不为0,
            if cur.next.val == 0:  # node.val = 0 则计数一次,计数跳过非0的节点
                count += 1
            cur = cur.next
        return cur


def magic(link, s):
    if not link:
        return None
    count = 1
    cur = link
    while count < s:  # 当链表中没有0时，退出循环

        for i in range(1, s+1):
            # 赋值 [1,s+1],
            cur.next.val = i  # 每次赋值给首节点
            cur = cur.next  # 第一个节点作为尾节点，第二个节点作为首节点
            # print("The link changed:", end=" ")
            # for node in LCLink.p_link(cur):
            #     print(node, end=" ")
            # print()

            if i < s:  # 当link中不存在0时跳出循环
                # print("Rest link:", end=" ")
                cur = LCLink.res_link(cur, i+1)  # 重置link的顺序，返回尾节点
                # for node in LCLink.p_link(cur):
                #     print(node, end=" ")
                # print()
                # print("=" * 25)
                count += 1
    while cur.next.val != 1:  # 重置cur顺序，从1开始
        cur = cur.next
    return cur


if __name__ == "__main__":
    s = 13
    _list = [0] * s
    # _list = list(range(1, s))
    # print(_list)
    link = LCLink.c_link(_list)
    # print("The origin link is:", end=" ")
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("="*25)

    # 从第s个位置重置link
    # s = 2
    # link = LCLink.res_link(link, s)
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("="*25)

    magic_link = magic(link, s)
    print("The final order of link is: ", end="")
    for node in LCLink.p_link(magic_link):
        print(node, end=" ")
    print()

