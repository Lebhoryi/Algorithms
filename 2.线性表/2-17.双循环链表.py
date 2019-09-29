# coding=utf-8
'''
@ Summary: 输入26个大写字母，接着输入s，第s+1个节点作为首节点，输出link
@ Update:  

@ file:    2-17.双循环链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-29 下午6:42
'''

class Node(object):
    def __init__(self, val):
        self.val = val  # 数据域
        self.prev = None  # 前驱
        self.next = None  # 后置

    def __repr__(self):
        return str(self.val)


class DLink(object):
    @ staticmethod
    def c_link(vals):
        # 创建双向链表
        if not vals:
            return None
        head = Node(len(vals))  # head node
        move = head  # move node
        for val in vals:
            tmp = Node(val)
            tmp.prev = move
            move.next = tmp
            move = tmp
        return head.next
        # return move

    @ staticmethod
    def p_link(link):
        # print link
        if not link:
            return None
        cur = link
        while cur:
            yield cur.val
            cur = cur.next
            # cur = cur.prev
        # yield cur.val



class DLCLink(object):
    @ staticmethod
    def c_link(vals):
        # create 双向循环链表
        if not vals:
            return None
        head = Node(len(vals))  # head node
        move = head   # move node
        for i in range(len(vals)):
            tmp = Node(vals[i])

            # add node
            tmp.next = tmp if i == 0 else move.next
            # print("tmp.next: ", tmp.next )
            tmp.prev = tmp if i == 0 else move
            # print("tmp.prev: ", tmp.prev)
            move.next = tmp
            # print("move.next: ", move.next)
            move.next.prev = tmp
            # print("move.next.prev: ", move.next.prev)
            # move node
            move = tmp
        print(tmp.prev)
        return move  # 返回尾节点
        # return head.next

    @ staticmethod
    def p_link(link):
        # print link
        if not link:
            return None
        cur = link.next
        # cur = link.prev
        while cur.next != link.next:
            yield cur.val
            cur = cur.next
            # cur = cur.prev
        yield cur.val

    @ staticmethod
    def l_link(link):
        # lenth of link
        if not link:
            return  None
        cur, count = link.next, 1
        while cur.next != link.next:
            cur = cur.next
            count += 1
        return count


    @ staticmethod
    def res_link(link, s, l_link):
        # 第s+1个节点作为首节点
        if not link or s == 0:
            return None
        if s > 0:
            s = s % l_link if s > l_link else s
            cur, count = link.next, 1
            while count < s:  # 找到第s个点
                cur = cur.next
                count += 1
            return cur
        else:
            s = -s
            s = s % l_link if s > l_link else s
            cur, count = link, 0
            while count < s:  # 找到第s个点
                cur = cur.prev
                count += 1
            return cur



if __name__ == "__main__":
    _list = list(range(1, 6))

    # print link
    print("双向链表： ", end="")
    link = DLink.c_link(_list)
    for node in DLink.p_link(link):
        print(node, end=" ")
    print()

    print("双向循环链表： ", end="")
    d_link = DLCLink.c_link(_list)
    for node in DLCLink.p_link(d_link):
        print(node, end=" ")
    print()
    print("="*30)

    # 链表长度
    lenth_link = DLCLink.l_link(d_link)
    # print("The lenth of link: {}.".format(lenth_link))

    # 重置链表
    s = -2
    d_link = DLCLink.res_link(d_link, s, lenth_link)
    print("重置双向循环链表： ", end="")
    for node in DLCLink.p_link(d_link):
        print(node, end=" ")
    print()
    print("="*30)