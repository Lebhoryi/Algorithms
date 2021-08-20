[TOC]

# 一、图的基础知识

### 1. 定义

- 图：顶点的有穷非空集合和顶点之间边的集合组成，通常表示为：G（V,E），其中G表示为一个图，V表示顶点集合，G表示边的集合

- 顶点：和线性表、树不同，图中不可以没有顶点

- 边、弧

- 按照方向分为无向图和有向图

- 按照边、弧的多少分为稠密图和稀疏图

- 权、网

- 子图

- 连通图

- 路径、环

  ![图](https://python-data-structures-and-algorithms.readthedocs.io/zh/latest/18_%E5%9B%BE%E4%B8%8E%E5%9B%BE%E7%9A%84%E9%81%8D%E5%8E%86/graph_road.png)

# 二、图的存储方式

### 1. 最常用的方法1-邻接表

- 邻接表法：数组与链表相结合的存储方法称为邻接表（Adjacency List）

  ![邻接表法](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170204571-1413258317.png)

  ![](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170205961-628372598.png)


### 2. 最常用的方法2-邻接矩阵

- 邻接矩阵：图的邻接矩阵（Adjacency Matrix）存储方式使用过两个数组来表示图。一个一维数组存储图中顶点信息，一个二维数组（称为邻接矩阵）存储图中的边或弧的信息

  ![邻接矩阵](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170155946-1728532738.png)
  
- 缺点：

  对于边数相对顶点较少的图，这种结构是存在对存储空间的极大浪费

  ![](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170200852-240259435.png)

### 3. 其他

- 十字链表

  ![十字链表](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170212211-373775021.jpg)

  ![](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170212977-1917645929.png)

- 邻接多重表 - 无向图的优化存储

  ![邻接多重表](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170213883-1468170253.png)

  ![](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170214571-314198936.png)

- 边集数组

  ![](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170217508-516819461.png)

  ![边集数组](https://images2015.cnblogs.com/blog/1007623/201706/1007623-20170601170216477-516473265.png)

  

# 三、图的遍历（重点）

### 1.深度优先遍历 DFS

```python
# coding=utf-8
'''
@ Summary: DFS: Depdth First Search，深度优先搜索
@ Update:  

@ file:    5-2.DFS.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-12-4 下午2:01
'''
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

seen = set()

def DFS(graph, s):
    if s not in seen:
        print(s)
        seen.add(s)
    for node in graph[s]:
        if node not in seen:
            DFS(graph, node)

def dfs(graph, s):
    """ stack """
    stack = [s]  # stack
    seen = {s}  # set()
    while stack:
        cur_node = stack.pop()  # LIFO
        print(cur_node)
        for node in graph[cur_node]:
            if node not in seen:
                stack.append(node)
                seen.add(node)


print("dfs:")
DFS(graph, "E")
```



### 2. 广度优先遍历 BFS

```python
# coding=utf-8
'''
@ Summary: BFS: Breadth First Search，广度优先搜索，队列
@ Update:  

@ file:    5-1.BFS.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-12-4 下午1:10
'''

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

def BFS(graph, s):
    queue = [s]
    seen = {s}  # 判断是否遍历过
    while queue:
        cur_node = queue.pop(0)
        print(cur_node)
        for node in graph[cur_node]:
            if node not in seen:
                queue.append(node)
                seen.add(node)


print("bfs:")
BFS(graph, "E")
```

### 3. 其他

以下均为涉及，将来要涉及

> - [数据结构之图](https://www.zybuluo.com/guoxs/note/249812)

> - 五、最小生成树
>   - [5.1 普里姆（Prim）算法](https://www.zybuluo.com/guoxs/note/249812#51-普里姆prim算法)
>   - [5.2 克鲁斯卡尔（Kruskal）算法](https://www.zybuluo.com/guoxs/note/249812#52-克鲁斯卡尔kruskal算法)
> - 六、最短路径
>   - [6.1 迪杰斯特拉（Dijkstra）算法](https://www.zybuluo.com/guoxs/note/249812#61-迪杰斯特拉dijkstra算法)
>   - [6.2 弗洛伊德（Floyd）算法](https://www.zybuluo.com/guoxs/note/249812#62-弗洛伊德floyd算法)
> - 七、拓扑排序
>   - [7.1 拓扑排序介绍](https://www.zybuluo.com/guoxs/note/249812#71-拓扑排序介绍)
>   - [7.2　拓扑排序算法](https://www.zybuluo.com/guoxs/note/249812#72-拓扑排序算法)
> - 八、关键路径
>   - [8.1 关键路径算法原理](https://www.zybuluo.com/guoxs/note/249812#81-关键路径算法原理)
>   - [8.2 关键路径算法](https://www.zybuluo.com/guoxs/note/249812#82-关键路径算法)

