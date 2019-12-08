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

GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
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