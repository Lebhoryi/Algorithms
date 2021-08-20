[TOC]



> - 正在学习的算法课程：《数据结构与算法之美》& "小甲鱼数据结构"
> - 传送门： [https://time.geekbang.org/column/126](https://time.geekbang.org/column/126)
> - 新发现的宝贝1：[黑马数据结构](https://www.bilibili.com/video/av50524094)
> - 文稿来源1：[https://www.ranxiaolang.com/static/python_algorithm/chapter6/section2.html](https://www.ranxiaolang.com/static/python_algorithm/chapter6/section2.html)
> - 文稿来源2：[https://python-data-structures-and-algorithms.readthedocs.io/zh/latest/12_%E5%9F%BA%E6%9C%AC%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95/basic_sort/](https://python-data-structures-and-algorithms.readthedocs.io/zh/latest/12_基本排序算法/basic_sort/)
> - 代码传送门：[https://github.com/Lebhoryi/Algorithms/tree/master/6.%E6%8E%92%E5%BA%8F](https://github.com/Lebhoryi/Algorithms/tree/master/6.排序)
> - 三大经典排序以及升级类排序
> - 2020/01/03



# 一、基本排序算法

![经典排序](https://static001.geekbang.org/resource/image/fb/cd/fb8394a588b12ff6695cfd664afb17cd.jpg)

> 带着问题去学习：
>
> Q：插入排序和冒泡排序的时间复杂度相同，都是 O(n2)，在实际的软件开发里，为什么我们更倾向于使用插入排序算法而不是冒泡排序算法呢？

## 0.比较分析算法

- 算法的执行效率

    - 时间复杂度

    - 时间复杂度的系数、常熟、阶数

    - 比较次数和交换次数（经典排序算法都是基于比较的算法

- 算法的内存消耗

    - **原地排序**(Sorted in place)：特指空间复杂度是 O(1) 的排序算法

- 算法的稳定性

    - **稳定性**：稳定排序算法会让原本有相等键值的纪录维持相对次序。

	也就是如果一个排序算法是稳定的，当有两个相等键值的纪录R和S，且在原本的列表中R出现在S之前，在排序过的列表中R也将会是在S之前。

## 1.  冒泡排序

### a. 概念

**冒泡排序**（英语：Bubble Sort）是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

![冒泡排序第一次](https://www.ranxiaolang.com/static/python_algorithm/images/bubblesort.jpg)

那么我们需要进行n-1次冒泡过程，每次对应的比较次数如下图所示：

![](https://www.ranxiaolang.com/static/python_algorithm/images/compare.bmp)

### b. 源码：

```python
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
        # print(alist)
        count = 0  # 面试加分项
        for i in range(n-j-1):
            # 从头走到尾
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:  # 如果count 为0，是最优情况，不用排序
            return alist
    return alist
```

### c.  时间复杂度

- 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
- 最坏时间复杂度：O(n2)
- 稳定性：稳定

### d.动画效果

![bubble](https://www.ranxiaolang.com/static/python_algorithm/images/bubble.gif)

## 2.插入排序

### a. 概念

​	插入排序（英语：Insertion Sort）是一种简单直观的排序算法。

​	将数组中的数据分为两个区间，**已排序区间**和**未排序区间**。初始已排序区间只有一个元素，就是数组的第一个元素。插入算法的**核心思想**是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。重复这个过程，直到未排序区间中元素为空，算法结束

![insert](https://www.ranxiaolang.com/static/python_algorithm/images/Insertion-sort-example.gif)

### b. 源码

```python
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
```

### c. 时间复杂度

- 最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
- 最坏时间复杂度：O(n2)
- 稳定性：稳定

###　d. 动画效果

![insert](https://www.ranxiaolang.com/static/python_algorithm/images/insert.gif)

## 3. 选择排序

### a. 概念

选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

![Selection-Sort-Animation](https://www.ranxiaolang.com/static/python_algorithm/images/Selection-Sort-Animation.gif) 

红色表示当前最小值，黄色表示已排序序列，蓝色表示当前位置。

### b. 源码
```python
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
        # print(alist)
        for j in range(i+1, n):
            # 寻找最小元素的下标
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

alist = [54,226,93,17,77,31,44,55,20]
select_sort(alist)
print(alist)
```

###  c. 时间复杂度

- 最优时间复杂度：O(n2)
- 最坏时间复杂度：O(n2)
- 稳定性：不稳定（考虑升序每次选择最大的情况）

###  d. 选择排序演示

![selection](https://www.ranxiaolang.com/static/python_algorithm/images/selection.gif)

>Q: 开篇问题，为什么选择插入而不是冒泡？
>
>A: 在c语言或者java中，插入排序只需要1个赋值操作，而冒泡排序则需要3个，如下所示
>
>```java
>// 冒泡排序中数据的交换操作：
>if (a[j] > a[j+1]) { // 交换
>   int tmp = a[j];
>   a[j] = a[j+1];
>   a[j+1] = tmp;
>   flag = true;
>}
>
>// 插入排序中数据的移动操作：
>if (a[j] > value) {
>  a[j+1] = a[j];  // 数据移动
>} else {
>  break;
>}
>a[j+1] = value;  // 插入数据
>```

# 二、升级版排序算法

三大基础排序算法的时间复杂度都是$O(n^2)$，接下来介绍的时间复杂度均是$O(nlog(n))$

## 1. 归并排序

### a. 概念

归并排序(merge sort)是采用**分治法**的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

![Merge-sort-example](https://www.ranxiaolang.com/static/python_algorithm/images/Merge-sort-example.gif)

### b. 源码

```python
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
    result = []
    a, b = 0, 0
    while a < len(list_a) and b < len(list_b):
        if list_a[a] >= list_b[b]:
            result.append(list_b[b])
            b += 1
        else:
            result.append(list_a[a])
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
```

### c. 时间复杂度

- 最优时间复杂度：O(nlogn)
- 最坏时间复杂度：O(nlogn)
- 空间复杂度： O(n)
- 稳定性：稳定

## 2. 快速排序

### a. 概念

快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

- 步骤：
  - 从数列中挑出一个元素，称为"基准"（pivot），
  - 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
  - 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

![](https://python-data-structures-and-algorithms.readthedocs.io/zh/latest/13_%E9%AB%98%E7%BA%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95/quick_sort.png)

### b. 源码

暴力版本

```python
def q_sort(alist):
    # 暴力 不建议
    if not alist or len(alist) < 2:  return alist
    pivot_index = 0
    pivot = alist[pivot_index]
    left = [i for i in alist[pivot_index+1:] if i <= pivot]
    right = [i for i in alist[pivot_index+1:] if i > pivot]
    return q_sort(left) + [pivot] + q_sort(right)
```

优化版本，只在原数组进行操作，不生成新的数组

```python
# coding=utf-8
'''
@ Summary: quick sort
@ Update:  https://www.ranxiaolang.com/static/python_algorithm/chapter6/section4.html

@ file:    6-5.快速排序.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    20-1-1 下午10:44
'''
def quick_sort(alist, beg, end):
    if not alist or beg >= end:  return
    pivot = alist[beg]
    left, right = beg, end  # 左右起始值
    while left < right:
        # 左移 high
        while left < right and alist[right] >= pivot:
            right -= 1
        # alist[left] = alist[right]
        # 右移 left
        while left < right and alist[left] < pivot:
            left += 1
        alist[left], alist[right] = alist[right], alist[left]
	
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[left] = pivot
    # 对 left 左边进行快排
    quick_sort(alist, beg, left-1)
    # 对 left 右边进行快排
    quick_sort(alist, left+1, end)



if __name__ == "__main__":
    alist = list(range(10))
    import random
    random.shuffle(alist)
    print("The initial list: \n{}".format(alist))
    alist = sorted(alist)
    # alist.sort()
    quick_sort(alist, 0, len(alist)-1)
    print("The sorted list: \n{}".format(alist))
```



### c.  时间复杂度

- 最优时间复杂度：O(nlogn)
- 最坏时间复杂度：O(n2)
- 稳定性：不稳定

### d. 动画效果

![quicksort](https://www.ranxiaolang.com/static/python_algorithm/images/quicksort.gif)

## 3. 希尔排序

### a. 概念

希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。

基本思想是将数组列在一个表中并对列分别进行插入排序，重复这过程

例如，假设有这样一组数[ 13 14 94 33 82 25 59 94 65 23 45 27 73 25 39 10 ]，如果我们以步长为5开始进行排序，我们可以通过将这列表放在有5列的表中来更好地描述算法，这样他们就应该看起来是这样(竖着的元素是步长组成)：

```
13 14 94 33 82
25 59 94 65 23
45 27 73 25 39
10
```

然后我们对每列进行排序：

```
10 14 73 25 23
13 27 94 33 39
25 59 94 65 82
45
```

将上述四行数字，依序接在一起时我们得到：[ 10 14 73 25 23 13 27 94 33 39 25 59 94 65 82 45 ]。这时10已经移至正确位置了，然后再以3为步长进行排序：

```
10 14 73
25 23 13
27 94 33
39 25 59
94 65 82
45
```

排序之后变为：

```
10 14 13
25 23 33
27 25 59
39 65 73
45 94 82
94
```

最后以1步长进行排序（此时就是简单的插入排序了）

### b. 源码

```python
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
```

### c.  时间复杂度

- 最优时间复杂度：根据步长序列的不同而不同
- 最坏时间复杂度：O(n2)
- 稳定想：不稳定

### d. 动画效果

![shellsort](https://www.ranxiaolang.com/static/python_algorithm/images/shellsort.gif)

# 三、再高级一点的排序 - 线性排序（拓展）

## 1. 桶排序（Bucket sort）

### a. 概念

核心思想是将要排序的数据分到几个有序的桶里，每个桶里的数据再进行**快排**。桶内排完序之后，再把每个桶里的数据按照顺序依次取出，组成的序列就是有序的了。

![img](https://static001.geekbang.org/resource/image/98/ae/987564607b864255f81686829503abae.jpg)

### b. 适用场景

​	**桶排序比较适合用在外部排序中**。所谓的外部排序就是数据存储在外部磁盘中，数据量比较大，内存有限，无法将数据全部加载到内存中。

​	举例：比如说我们有 10GB 的订单数据，我们希望按订单金额（假设金额都是正整数）进行排序，但是我们的内存有限，只有几百 MB，没办法一次性把 10GB 的数据都加载到内存中。这个时候该怎么办呢？

​	划分区间，分别加载

### c.  时间复杂度

- 最优时间复杂度：O(n)

  ​	如果要排序的数据有 n 个，我们把它们均匀地划分到 m 个桶内，每个桶里就有 k=n/m 个元素。每个桶内部使用快速排序，时间复杂度为 O(k * logk)。m 个桶排序的时间复杂度就是 O(m * k * logk)，因为 k=n/m，所以整个桶排序的时间复杂度就是 O(n*log(n/m))。当桶的个数 m 接近数据个数 n 时，log(n/m) 就是一个非常小的常量，这个时候桶排序的时间复杂度接近 O(n)

- 最坏时间复杂度：O(nlogn)

## 2. 计数排序（Counting sort）

### a. 概念

​	计数排序其实是桶排序的一种特殊情况。当要排序的 n 个数据，所处的范围并不大的时候，比如最大值是 k，我们就可以把数据划分成 k 个桶。每个桶内的数据值都是相同的，省掉了桶内排序的时间。

​	借助另外一个数组来计数，c数组里面是各个元素个数

![img](https://static001.geekbang.org/resource/image/1d/84/1d730cb17249f8e92ef5cab53ae65784.jpg)

### b. 适用场景

计数排序只能用在数据范围不大的场景中，如果数据范围 k 比要排序的数据 n 大很多，就不适合用计数排序了。而且，计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。

# 三、小结

## 1. 如何选择合适的排序算法

![img](https://static001.geekbang.org/resource/image/1f/fd/1f6ef7e0a5365d6e9d68f0ccc71755fd.jpg)

​	如果对小规模数据进行排序，可以选择时间复杂度是$O(n^2)$  的算法；如果对大规模数据进行排序，时间复杂度是$O(nlogn)$ 的算法更加高效

​	归并和快排优先选择快排，归并空间耗费多

## 2. 优化快排

- 取中法
- 随机法