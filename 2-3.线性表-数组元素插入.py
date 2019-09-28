# coding=utf-8
'''
@ Summary: 在线性表中插入和删除一个元素
@ Update:  

@ file:    2-3.线性表-数组元素插入操作.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-24 下午3:39
'''

def list_insert(l, i, new_elem):
    if not l or i < 0 or i > len(l):
        return None
    if len(l) <= max_lenth:
        l.insert(i, new_elem)
    return l

'''
python list 删除的常用三种方法：

    1. del list[3]
    2. list.pop(index)  # 删除索引指向的元素
    3. list.remove(elem)  # 删除指定的元素
'''

def list_del(l, i):
    if not l or i < 0 or i > len(l):
        return None
    l.pop(i-1)
    return l

if __name__ == "__main__":
    l = [1, 2, 3]
    i, new_elem = 1, 5
    global max_lenth
    max_lenth = 7
    result = list_insert(l, i, new_elem)
    print(result)
    result2 = list_del(l, i)
    print(result2)
