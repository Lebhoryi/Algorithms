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

