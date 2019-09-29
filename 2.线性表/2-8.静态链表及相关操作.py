# coding=utf-8
'''
@ Summary: 用数组实现链表及操作
           数组储存[data, cur]，data是当前值，cur是下一个节点的下标。
           其中头节点的cur储存的是第一个节点的下标，最后一个固定长度的节点的cur
           存储的是头节点的下标
@ Update:  代码实现的有问题 ，没有修改， 2919/09/29

@ file:    2-8.静态链表及相关操作.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-26 下午4:20
'''


class Link(object):
    @staticmethod
    def c_link(l, maxsize = 1000):
        if not l or len(l) > maxsize:
            return None
        node = [None, 1]
        link = [node] + [[None, i] for i in range(2, maxsize)] \
               + [[None, 0]]
        for i in range(len(l)):
            if i != len(l) - 1:
                node = [l[i], i+2]
            else:
                node = [l[i], 0]
            link[i+1] = node
        return link

    @staticmethod
    def p_link(links):
        if not links:
            return None
        for link in links:
            print(link[0], end=" ")
        print()


    @staticmethod
    def l_link(links):
        if not links:
            return None
        count = 0
        for link in links:
            if link[0]:
                count += 1
        return count


    @staticmethod
    def i_link(links, n_cur, n_data, l_link):
        # 在第s个节点之后插入node节点
        node = [n_data, n_cur]
        if not links or n_cur < 0 or n_cur > l_link:
            return None
        link1 = links[:n_cur+1]
        link1.append(node)
        link2 = []
        for i in range(n_cur, l_link):
            link = [links[i][0], links[i][1] + 1]
            link2.append(link)
        return link1 + link2 + links[l_link+2:]



if __name__ == "__main__":

    list_a = [1, 3, 5, 2, 4]
    maxsize = 10
    link_a = Link.c_link(list_a, maxsize)  # 创建链表
    Link.p_link(link_a)  # 打印链表，指定长度
    lenth_link = Link.l_link(link_a)  # 统计链表长度

    # 插入元素node，在第二个位置插入2，node = [date, cur]
    n_data, n_cur = 2, 2
    link_a = Link.i_link(link_a, n_cur, n_data, lenth_link)
    Link.p_link(link_a)



