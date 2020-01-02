# coding=utf-8
'''
@ Summary: insert sort
@ Update:  

@ file:    6-3.插入排序.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-12-19 下午12:50
'''
def insert_sort(alist):
    if not alist:  return
    n = len(alist)
    for i in range(1, n):
        # i = [1, 2, 3, ..., n-1]
        for j in range(i, 0, -1):
            # j = [i, i-1, ..., 1]
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            # else:
            #     break

    return alist

if __name__ == "__main__":
    alist = list(range(10))
    import random
    random.shuffle(alist)
    print(alist)
    alist = insert_sort(alist)
    print(alist)