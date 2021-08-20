# coding=utf-8
'''
@ Summary: 进栈：元素入队列A(后进先出)
           出栈：判断如果队列A只有一个元素，则直接出队。否则，把队A中的元素出队并入队B，
           直到队A中只有一个元素，再直接出队。为了下一次继续操作，互换队A和队B。
@ Update:

@ file:    3-16.2队列实现栈.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-22 下午7:12
'''
class SQueue(object):
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def is_empty(self):
        return self.queueA == [] and self.queueB == []

    def enqueue(self, elem):
        # 入队
        self.queueA.append(elem)

    def dequeue(self):
        #出队
        if self.is_empty():
            return None
        # if len(self.queueA) == 1:
        #     return self.queueA.pop()
        while len(self.queueA) > 1:
            self.queueB.append(self.queueA.pop(0))
        self.queueA, self.queueB = self.queueB, self.queueA
        return self.queueB.pop()


if __name__ == "__main__":
    sq = SQueue()
    for i in range(1, 7):
        sq.enqueue(i)
    print(sq.dequeue())
    sq.enqueue(3)
    print(sq.dequeue())
    print(sq.dequeue())


