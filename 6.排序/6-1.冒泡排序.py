# coding=utf-8
'''
@ Summary: bubble sort
@ Update:  

@ file:    6-1.冒泡排序.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-12-15 下午7:32
'''
def bubble_sort(alist):
    """冒泡排序"""
    if not alist:  return
    n = len(alist)
    for j in range(n-1):
        print(alist)
        count = 0  # 面试加分项
        for i in range(n-j-1):
            # 从头走到尾
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return alist
    return alist

if __name__ == "__main__":
    alist = list(range(10))
    import random
    random.shuffle(alist)
    alist1 = bubble_sort(alist)
    assert alist1 == sorted(alist)