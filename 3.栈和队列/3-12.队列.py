# coding=utf-8
'''
@ Summary: 链表实现队列
@ Update:  

@ file:    3-12.队列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-17 上午10:29
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LQueue(object):
    def __init__(self):
        self.front = Node(0)
        self.rear = Node(0)

    def is_empty(self):
        # 是否为空
        return self.front.val == self.rear.val

    def enqueue(self, elem):
        # 入队
        elem = Node(elem)
        if self.is_empty():
            # 第一个元素进队列
            self.front.next = elem
        self.rear.next = elem
        self.rear = elem


    def dequeue(self):
        # 出队
        if self.is_empty():
            return None
        del_node = self.front.next
        if self.front.next == self.rear:
            # 当只有一个元素的时候
            self.front = self.rear
        self.front.next = self.front.next.next
        return del_node.val

    def p_queue(self):
        # print queue
        if self.is_empty():
            return None
        tmp = self.front.next
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    lq = LQueue()
    data = "abcd"
    for item in data:
        lq.enqueue(item)  # 入队
    lq.p_queue()  # 打印
    print(lq.dequeue())  # 出队
    lq.p_queue()

