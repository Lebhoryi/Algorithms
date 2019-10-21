# coding=utf-8
'''
@ Summary: 顺序表实现循环队列
@ Update:  

@ file:    3-14.循环队列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-21 下午9:43
'''
class SQueue(object):
    def __init__(self, maxsize):
        self._queue = [None] * maxsize  # 空队
        self.maxsize = maxsize  # 最大size
        self.front = 0  # 指向队列首个元素
        self.rear = 0  # 指向队列末尾元素的下一个位置

    def is_empty(self):
        # 队列是否为空
        return self.front == self.rear

    def enqueue(self, elem):
        if (self.rear + 1) % self.maxsize == self.front:
            # 队列已满
            print("队列已经满员..")
        self._queue[self.rear] = elem
        self.rear = (self.rear+1) % self.maxsize

    def dequeue(self):
        if self.is_empty():
            return None
        del_elem = self._queue[self.front]
        self._queue[self.front] = None
        self.front = (self.front + 1) % self.maxsize
        return del_elem

    def p_queue(self):
        if self.is_empty():
            return None
        print(self._queue)


if __name__ == "__main__":
    s = "abcdde"
    sq = SQueue(15)  # 循环队列
    for item in range(10):
        # 入队
        sq.enqueue(item)
    sq.p_queue()  # 原始队列
    for i in range(5):  # 删除队头的5个元素：0~4
        sq.dequeue()
    sq.p_queue()
    for i in range(8):  # 从队尾增加8个元素：0~7
        sq.enqueue(i)
    sq.p_queue()
