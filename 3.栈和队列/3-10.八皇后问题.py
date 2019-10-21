# coding=utf-8
'''
@ Summary: 递归实现八皇后问题
@ cankao:  https://www.cnblogs.com/tomhawk/p/7454558.html
@ update:  此问题难点在于如何把控递归函数的返回条件，一种条件是8个皇后放置完成后，返回成
           功，一种条件是该行中已经没有可以放置的位置，此时返回失败，需要重新放置。此时要
           额外注意，所谓的“重新放置”指的并不是将所有皇后清除重新来过，而是只返回上一层，
           将上一个导致本次放置失败的皇后进行清除，然后重新更新其位置，通过逐级放置、或逐
           级回溯可以达到遍历所有情况找到所有解

@ file:    3-10.八皇后问题.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-9 上午9:51
'''
def conflict(nexty, chess):
    # 冲突判断
    ########################################################
    # 1. 同一列: nexty in chess
    # 2. \: for i in range(len(chess)):
    #           nexty - len(chess) = chess[i] - i
    # 3. /: for i in range(len(chess)):
    #           nexty + len(chess) = chess[i] + i
    ########################################################

    len_chess = len(chess)
    if nexty in chess:
        return True
    for i in range(len_chess):
        if abs(chess[i]-nexty) == len_chess-i:
            return True
    return False


def EightQueens(row, chess):
    global count
    if len(chess) == row:
        count += 1
        print(chess)
        # print(count)
    for pos in range(row):
        if not conflict(pos, chess):
            chess1 = chess[:]  # 为了防止回退的时候更改原chess
            print(chess)
            chess1.append(pos)  # 当不满足时回溯到上一个状态
            EightQueens(row, chess1)
    return count

if __name__ == "__main__":
    chess = []
    count = 0
    EightQueens(8, chess)

    print(count)
