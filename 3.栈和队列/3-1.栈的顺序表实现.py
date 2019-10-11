# coding=utf-8
'''
@ Summary: python中的list可以满足栈的操作，但是多了栈所没有的操作
           缺乏安全性，因此把list作为类的内部，作为实现基础
@ Update:  

@ file:    3-1.栈的顺序表实现.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-7 下午6:17
'''

class SStack(object):
    def __init__(self):
        self._elem = []

    def is_empty(self):
        # 是否空栈
        return self._elem == []

    def top(self):
        # 取栈顶元素
        if self.is_empty():
            return None
        return self._elem[-1]

    def push(self, elem):
        # 入栈
        return self._elem.append(elem)

    def pop(self):
        # 出栈
        if self.is_empty():
            return None
        return self._elem.pop()

if __name__ == "__main__":
    st1 = SStack()
    st1.push(3)
    # print(st1.top())
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())