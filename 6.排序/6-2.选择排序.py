# coding=utf-8
'''
@ Summary: select sort
@ Update:  

@ file:    6-2.选择排序.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-12-15 下午8:03
'''
def select_sort(alist):
    if not alist:  return
    n = len(alist)
    for i in range(n-1):
        min_index = i
        print(alist)
        for j in range(i+1, n):
            # 寻找最小元素的下标
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

    return alist

if __name__ == "__main__":
    alist = list(range(10))
    import random
    random.shuffle(alist)
    alist = select_sort(alist)
    print(alist)