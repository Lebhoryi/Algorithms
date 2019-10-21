# coding=utf-8
'''
@ Summary: 顺序队列
@ Update:  

@ file:    3-13.队列2.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-21 下午9:38
'''
class SQueue(object):
    def __init__(self):
        self._queue = []

    def is_empty(self):
        # 是否为空
        return self._queue == []

    def enqueue(self, elem):
        # 入队
        self._queue.insert(0, elem)

    def dequeue(self):
        # 出队列
        if self.is_empty():
            return None
        return self._queue.pop()

    def p_queue(self):
        # print queue
        if self.is_empty():
            return None
        print(self._queue)

if __name__ == "__main__":
    sq = SQueue()
    data = "abcd"
    for item in data:
        sq.enqueue(item)  # 入队
    sq.p_queue()  # 打印
    print(sq.dequeue())  # 出队
    sq.p_queue()