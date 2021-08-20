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
            if i == 0:  # 第一个节点循环自身
                tmp.next = tmp
                tmp.prev = tmp
            else:
                tmp.next = move.next
                tmp.prev = move
                move.next.prev = tmp
            move.next = tmp
            move = tmp

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
    def d_node(link, s, l_link):
        # del s node
        if not link or s == 0:
            return None
        count, cur = 0, link
        if s > 0:
            s = s % l_link if s > l_link else s
            while count < s:  # 找到第s-1个点
                cur = cur.next
                count += 1
        else:
            s = abs(s)
            s = s % l_link if s > l_link else s
            while count < s:  # 找到倒数第abs(s)个node
                cur = cur.prev
                count += 1
        # 删除第s个node
        cur.next = cur.next.next
        cur.next.next.prev = cur
        return link


    @ staticmethod
    def res_link(link, s, l_link):
        # 第s+1个节点作为首节点
        if not link or s == 0:
            return None
        count, cur = 0, link
        if s > 0:
            s = s % l_link if s > l_link else s
            while count < s:  # 找到第s-1个点
                cur = cur.next
                count += 1
        else:
            s = abs(s)
            s = s % l_link if s > l_link else s
            while count < s:  # 找到倒数第abs(s)个node
                cur = cur.prev
                count += 1
        return cur



if __name__ == "__main__":
    # _list = list(range(1, 6))
    _list = [chr(i) for i in range(65, 91)]
    # print link
    # print("双向链表： ", end="")
    # link = DLink.c_link(_list)
    # for node in DLink.p_link(link):
    #     print(node, end=" ")
    # print()

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
    s = -3
    d_link = DLCLink.res_link(d_link, s, lenth_link)
    print("重置双向循环链表： ", end="")
    for node in DLCLink.p_link(d_link):
        print(node, end=" ")
    print()
    print("="*30)

    d_link = DLCLink.d_node(d_link, s, lenth_link)
    print("删除第{}个节点： ".format(s), end="")
    for node in DLCLink.p_link(d_link):
        print(node, end=" ")
    print()
    print("="*30)