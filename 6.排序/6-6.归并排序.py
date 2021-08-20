# coding=utf-8
'''
@ Summary: merge sort
@ Update:  

@ file:    6-6.归并排序.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    20-1-2 下午3:34
'''
def merge_sorted_list(list_a, list_b):
    # 合并两个子序列
    list_new = []
    a, b = 0, 0
    while a < len(list_a) and b < len(list_b):
        if list_a[a] >= list_b[b]:
            list_new.append(list_b[b])
            b += 1
        else:
            list_new.append(list_a[a])
            a += 1

    # 把多余的数组放进新数组里
    list_new += list_a[a:]
    list_new += list_b[b:]

    return list_new



def merge_sort(alist):
    if not alist or len(alist) <= 1:
        return alist
    mid_index = len(alist) // 2


    left_half = merge_sort(alist[:mid_index])
    right_half = merge_sort(alist[mid_index:])

    # 合并两个子序列
    new_alist = merge_sorted_list(left_half, right_half)
    return new_alist


if __name__ == "__main__":
    alist = list(range(10))
    import random
    random.shuffle(alist)
    print("The initial list: \n{}".format(alist))
    alist = sorted(alist)
    # alist.sort()
    alist = merge_sort(alist)
    print("The sorted list: \n{}".format(alist))