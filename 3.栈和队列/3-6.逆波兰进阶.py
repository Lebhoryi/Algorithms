# coding=utf-8
'''
@ Summary: 中缀表达式转换为后缀表达式
@ Update:  

@ file:    3-6.逆波兰进阶.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-8 下午4:43
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LStack(object):
    def __init__(self):
        # 初始化 top node
        self._top = None

    def push(self, elem):
        # 入栈 self._top 始终指向first node
        elem = Node(elem)
        elem.next = self._top
        self._top = elem

    def pop(self):
        # 出栈 self._pop指向第二个节点, 返回第一个节点的值
        if not self._top:
            return None
        p = self._top
        self._top = self._top.next
        return p.val


def mid_2_after(l):
    # 中缀转后缀

    # 优先级
    ops_relu = {"+":1, "-":1,
                "*":2, "/":2,
                "(":1, ")":1}

    stack = LStack()  # 储存运算符和"（）"的栈
    lt = []  # 输出列表

    for item in l:
        # 遇到数字添加进列表中，非数字进行栈的相关操作
        try:
            item = int(item)
            lt.append(item)
        except ValueError:
            if item != ")":
                # 优先级顺序，栈顶的优先级高则弹出栈中所有元素
                if stack._top and ops_relu[item] < ops_relu[stack._top.val]:
                    while stack._top:
                        lt.append(stack.pop())
                stack.push(item)  # 入栈
            else:
                # 遇到")", 弹出栈中的元素, 直到"("为止
                while stack._top.val != "(":
                    lt.append(stack.pop())
                stack.pop()  # delete "("

    # 弹出栈中所有元素
    while stack._top:
        lt.append(stack.pop())

    return lt


if __name__ == "__main__":
    _input = "1 + ( 2 - 3 ) * 4 + 10 / 5"  # "1 2 3 - 4 * + 10 5 / +"
    _list = _input.split(" ")  # str to list
    print("The origin list is: {}.".format(_list))

    print(mid_2_after(_list))
