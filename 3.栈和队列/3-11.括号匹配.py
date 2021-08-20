# coding=utf-8
'''
@ Summary: 用链表实现括号匹配
@ Update:  用数组实现括号匹配

@ file:    3-11.括号匹配.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-15 上午11:20
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

    def is_emtpy(self):  # 判断是否为空
        return self.top == None

    def push(self, elem):  # 入栈
        elem = Node(elem)
        elem.next = self.top
        self.top = elem

    def pop(self):  # 弹出
        if self.is_emtpy():
            return None
        del_node = self.top
        self.top = self.top.next
        return del_node.val

    def p_stack(self):
        if self.is_emtpy():
            return None
        tmp = self.top
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next

    def p_top(self):
        if self.is_emtpy():
            return None
        return self.top.val


def check_parens(s):
    # 链表
    if not s:
        return None
    parents = "()[]{}"
    close_par = ")]}"
    st = LStack()
    opposite = {")":"(", "]":"[", "}":"{"}
    for item in s:
        if item in parents:
            st.push(item)
        if item in close_par:
            del_elem = st.pop()
            if opposite[del_elem] != st.p_top() or st.is_emtpy():
                return False
            else:
                st.pop()
    return not st

def is_valid(s):
    # 顺序表
    if not s:
        return None
    parents = "()[]{}"
    opposite = {")":"(", "]":"[", "}":"{"}
    st = []  # 栈
    for item in s:
        if item in parents:
            st.append(item)  # 入栈
        if item in opposite:
            del_elem = st.pop()  # 出栈
            if not st or st.pop() != opposite[del_elem]:  # 出栈的栈顶元素比较
                return False
        return not st

if __name__ == "__main__":
    s = "(){{}[]{}"

    if is_valid(s):
        print("'{}' is OK.".format(s))
    else:
        print("'{}' is not OK.".format(s))
