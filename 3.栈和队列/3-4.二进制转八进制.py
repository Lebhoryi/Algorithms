# coding=utf-8
'''
@ Summary: 用栈实现二进制转八进制
@ Update:  

@ file:    3-3.二进制转八进制.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-7 下午10:05
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
    _input = 11001001  # 初始值
    _list = list(map(int, str(_input)))  # int to list
    while len(_list) % 3 != 0:  # 三的倍数，不够补0
        _list.insert(0, 0)

    _list.insert(0, 0)  # 为了后面的while 循环到栈底的时候继续运行，增加一个0
    st1 = SStack()  # 二进制的栈
    st2 = SStack()  # 八进制的栈
    for i in _list:  # 二进制入栈
        st1.push(i)
    print(st1._elem)

    # 二进制 三个弹出，计算，压入八进制栈
    tmp = []  # 储存三个二进制数
    count = 1  # 计数
    while not st1.is_empty():
        if count < 4:
            # 找到三个二进制数
            tmp.append(str(st1.pop()))
            count += 1
        else:
            num = "".join(tmp)
            # 二进制转八进制
            num = int(num[2]) * 2**2 + int(num[1]) * 2**1 + \
                  int(num[0]) * 2**0
            st2.push(num)  # 入栈
            count = 1
            tmp = []

    print(st2._elem)