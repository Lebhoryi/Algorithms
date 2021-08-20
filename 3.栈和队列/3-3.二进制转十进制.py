# coding=utf-8
'''
@ Summary: 二进制转十进制,用栈实现
@ Update:  

@ file:    3-3.二进制转十进制.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-7 下午7:16
'''

class SStack(object):
    def __init__(self):
        self._elem = []

    def is_empty(self):
        # 是否空栈
        return self._elem == []

    def push(self, elem):
        # 入栈
        return self._elem.append(elem)

    def pop(self):
        # 出栈
        if self.is_empty():
            return None
        return self._elem.pop()

if __name__ == "__main__":
    _input = 1010110
    _list = list(map(int, str(_input)))

    st1 = SStack()
    for i in _list:
        st1.push(i)
    print(st1._elem)

    sum = count = 0
    while not st1.is_empty():
        # print(st1.pop(), end=" ")
        _pop = st1.pop()
        sum = sum + _pop * 2**count
        count += 1
    print(sum)
