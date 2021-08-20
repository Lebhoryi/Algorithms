# coding=utf-8
'''
@ Summary: https://www.bilibili.com/video/av58557186
@ Update:  

@ file:    3-18.八皇后2.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-25 下午4:14
'''
def valid(row, chess):
    # 判断是否有效
    for i in range(row):
        # 三个判断条件: \ / |
        if abs(chess[row] - chess[i]) == row - i \
                or chess[i] == chess[row]:
            return False
    return True

def Queens(n):
    ans = []  # 集合了所有答案
    def dfs(row, chess):
        # 深度优先遍历，递归
        if row == n:  # 递归终止条件，找到了一个符合条件的排列
            return ans.append(chess[:])
        for col in range(n):
            chess[row] = col
            if valid(row, chess):
                dfs(row+1, chess)

    dfs(0, [[] for _ in range(n)])

    return ans

if __name__ == "__main__":
    print(len(Queens(8)))

