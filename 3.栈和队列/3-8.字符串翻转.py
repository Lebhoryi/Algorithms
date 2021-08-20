# coding=utf-8
'''
@ Summary: 递归实现字符串翻转
@ Update:  

@ file:    3-8.字符串翻转.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-9 上午9:05
'''

def reverse(s):
    if len(s) <= 1:
        return s
    elif len(s) == 2:
        return s[1] + s[0]
    return s[-1] + reverse(s[:-1])

if __name__ == "__main__":
    s = "ABC"
    print(reverse(s))
