# coding=utf-8
'''
@ Summary: shell sort
@ Update:  

@ file:    6-4.希尔排序.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-12-30 下午4:15
'''
def shell_sort(alist, gap):
    if not alist:  return
    n = len(alist)
    # gap 变化到1之前的循环
    while gap > 0:
        # 插入算法与一般插入算法的区别 gap
        for j in range(gap, n):
            # j = [gap, gap+1, gap+2, ...,n-1]
            for i in range(j, 0, -1):
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap

        # 减小gap
        gap //= 2
    return alist


if __name__ == "__main__":
    alist = list(range(20))
    import random
    random.shuffle(alist)
    print("The initial list: \n{}".format(alist))
    alist = shell_sort(alist, gap=4)
    print("The sorted list: \n{}".format(alist))