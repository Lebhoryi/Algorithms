# coding=utf-8
'''
@ Summary: 剑指Offer-用两个栈来实现一个队列，完成队列的Push和Pop操作
@ Update:  (先进先出)

@ file:    3-15.2栈实现队列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-21 下午10:00
'''
import pysnooper

class SStack(object):

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def is_empty(self):
        # 判断satackA是否为空
        return self.stackA == []

    def push(self, elem):
        # stackA入栈
        self.stackA.append(elem)

    @pysnooper.snoop(watch=("self.stackA", "self.stackB"))
    def s_pop(self):
        # stackA 出栈 stackB 入栈
        if self.stackB:
            return self.stackB.pop()
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

    # def p_stack(self):
    #     if self.is_empty():
    #         return None
    #     print(self.stackA)
    #     print(self.stackB)


if __name__ == "__main__":
    ss = SStack()
    for i in range(7):
        ss.push(i)
    print(ss.s_pop())
    ss.push(8)
    print(ss.s_pop())

