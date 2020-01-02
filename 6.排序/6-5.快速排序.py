# coding=utf-8
'''
@ Summary: quick sort
@ Update:  https://www.ranxiaolang.com/static/python_algorithm/chapter6/section4.html

@ file:    6-5.快速排序.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    20-1-1 下午10:44
'''
def q_sort(alist):
    # 暴力 不建议
    if not alist or len(alist) < 2:  return alist
    pivot_index = 0
    pivot = alist[pivot_index]
    left = [i for i in alist[pivot_index+1:] if i <= pivot]
    right = [i for i in alist[pivot_index+1:] if i > pivot]
    return q_sort(left) + [pivot] + q_sort(right)



def quick_sort(alist, beg, end):
    if not alist or beg >= end:  return
    midValue = alist[beg]
    low, high = beg, end  # 左右起始值
    while low < high:
        # 左移 high
        while low < high and alist[high] >= midValue:
            high -= 1
        # alist[low] = alist[high]
        # 右移 low
        while low < high and alist[low] < midValue:
            low += 1
        alist[low], alist[high] = alist[high], alist[low]

    alist[low] = midValue
    # 对low 左边进行快排
    quick_sort(alist, beg, low-1)
    # 对low 右边进行快排
    quick_sort(alist, low+1, end)



if __name__ == "__main__":
    alist = list(range(10))
    import random
    random.shuffle(alist)
    print("The initial list: \n{}".format(alist))
    alist = sorted(alist)
    # alist.sort()
    quick_sort(alist, 0, len(alist)-1)
    print("The sorted list: \n{}".format(alist))