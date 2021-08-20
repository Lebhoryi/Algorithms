# coding=utf-8
'''
@ Summary: 逆波兰表达式,又称后缀表达式
@ Update:  

@ file:    3-4.逆波兰表达式.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-8 下午3:29
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LStack(object):
    def __init__(self):
        self.top = None

    def push(self, elem):
        # 入栈
        elem = Node(elem)
        elem.next = self.top
        self.top = elem

    def pop(self):
        # 出栈
        if not self.top:
            return None
        p = self.top
        self.top = self.top.next
        return p.val

    def p_link(self):
        if not self.top:
            return None
        while self.top:
            print(self.top.val, end=" ")
            self.top = self.top.next


def RPN(_list):
    # _int = [str(i) for i in range(20)]
    operators = "+-*/"

    st1 = LStack()
    for item in _list:
        try:
            item = int(item)
            st1.push(item)
        except ValueError:
            if item in operators:
                x2 = st1.pop()
                x1 = st1.pop()
                if item == "+":
                    st1.push(x1 + x2)
                elif item == "-":
                    st1.push(x1 - x2)
                elif item == "*":
                    st1.push(x1 * x2)
                elif item == "/":
                    st1.push(x1 / x2)

    return st1.top

if __name__ == "__main__":
    # _input = "1 2 - 4 5 + *"  # -9
    # _input = "5 6 7 + 8 * - 9 4 / +"  # -96.75
    # _input = "3 5 - 6 17 4 * + * 3 /"
    _input = "1 2 3 - 4 * + 10 5 / +"
    _list = _input.split(" ")  # str to list

    print(RPN(_list))



