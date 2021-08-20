# coding=utf-8
'''
@ Summary: dfs 最短路径
@ Update:  

@ file:    5-3.最短路径.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-12-4 下午2:42
'''

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

def bfs(graph, s):
    queue = [s]
    seen = {s}
    parent = {s : None}
    while queue:
        cur_node = queue.pop(0)
        for node in graph[cur_node]:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = cur_node
        # print(cur_node)
    return parent

parent = bfs(graph, "E")
for key, val in parent.items():
    print(key, ":", val)

# 从 E 走到 B
v = "B"
while v:
    print(v)
    v = parent[v]