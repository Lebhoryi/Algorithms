# coding=utf-8
'''
@ Summary: 递归实现汉诺塔
@ Update:  

@ file:    3-9.汉诺塔.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-9 上午9:19
'''
def hanoi(n, x, y, z):
    if n == 1:
        print(x + " --> " + z)
    else:
        # 将n-1个从X移动到Y上，借助Z
        hanoi(n-1, x, z, y)
        # 将第n个从X移动到Z上
        print(x + " --> " + z)
        # 将n-1个从Y移动到Z上，借助X
        hanoi(n-1, y, x, z)

if __name__ == "__main__":
    hanoi(4, "X", "Y", "Z")
