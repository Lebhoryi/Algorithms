# coding=utf-8
'''
@ Summary: 给定一个数组，一开始顺序从小变大，接着到达某个值之后，顺序从大变小，请设计一个复杂
           度为O(logn)的算法，找到这个最大值
           思路： 判断中点，舍掉左边或者右边
@ Update:  

@ file:    O(nlogn).py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-23 下午6:05
'''

def local_maximum(l):
    if not l:
        return None

    if len(l) == 1:
        return l[0]
    else:
        mid = int(len(l)/2)
        l = l[:mid+1] if l[mid] >= l[mid+1] else l[mid+1:]
        return local_maximum(l)

def local_maximum2(l):
    if not l:
        return None
    left = 0
    right = len(l) -1
    while left < right:
        mid = int((right + left)/2)
        if l[mid] > l[mid+1]:
            right = mid
        else:
            left = mid + 1

    return l[left]


if __name__ == "__main__":

    # import sys
    # _list = list(map(int, sys.stdin.readline().strip().split()))

    _list = [1, 2, 3, 4, 3, 2]
    result = local_maximum2(_list)
    print(result)
