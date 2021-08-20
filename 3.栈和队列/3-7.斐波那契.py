# coding=utf-8
'''
@ Summary: 斐波那契
@ Update:  

@ file:    3-7.斐波那契.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-8 下午10:18
'''

def fib(n):
    # 递归
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib2(n):
    # 生成器
    if n < 0:
        return None
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, b + a


if __name__ == "__main__":
    for i in fib2(5):
        print(i)

