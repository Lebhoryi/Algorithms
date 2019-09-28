# coding=utf-8
'''
@ Summary: 从线性表中获得元素
@ Update:  

@ file:    2-2.线性表-数组元素查找.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-24 下午3:33
'''

def get_elem(i, l):
    if not l:
        return None
    return l[i-1]

if __name__ == "__main__":
    l = [1, 2, 3]
    i = 1
    result = get_elem(i, l)
    print(result)
