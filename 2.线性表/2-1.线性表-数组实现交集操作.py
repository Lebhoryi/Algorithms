# coding=utf-8
'''
@ Summary: 有数组A和B，实现AUB
@ Update:  

@ file:    2-1.线性表-数组实现交集操作.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-24 下午3:18
'''

def union(la, lb):
    for i in lb:
        if i not in la:
            la.append(i)

    return la

if __name__ == "__main__":
    la = [1, 2, 3]
    lb = [2, 3, 4]
    result = union(la, lb)
    print(result)
