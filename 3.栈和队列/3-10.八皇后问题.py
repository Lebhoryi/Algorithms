# coding=utf-8
'''
@ Summary: 递归实现八皇后问题
@ cankao:  https://www.cnblogs.com/tomhawk/p/7454558.html

@ file:    3-10.八皇后问题.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-9 上午9:51
'''
def conflict(pos, chess):
    # 冲突判断
    len_chess = len(chess)
    for i in range(len_chess):
        if abs(chess[i]-pos) in (0, len_chess-i):
            return True
    return False


def EightQueen(n, chess):
    global count
    if len(chess) == n:
        count += 1
        print(chess)
    else:
        for pos in range(n):
            if not conflict(pos, chess):
                chess1 = []
                for i in chess:
                    chess1.append(i)
                chess1.append(pos)
                EightQueen(n, chess1)
    return count

if __name__ == "__main__":
    # n = 4
    # chess = [[0]*n for _ in range(n)]
    chess = []
    count = 0
    EightQueen(8, chess)

    print(count)
