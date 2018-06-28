# 8 x 8 のチェスの盤面に 8 個の「女王 ( queen ) 」を置く時、
# 全ての女王がお互いを取ることができないような配置を
# すべて表示するプログラムを作成しなさい
#
import csv

def init_queen(n):
    global q_pos, q_row, q_se, q_sw

    q_pos = [0] * n #クイーンの位置（インデックスが列、値が行を表す）
    q_row = [True] * n #置けるクイーンの行
    q_se = [True] * ((2 * n) - 1) #置けるクイーンの＼方向（斜めの本数に対応）
    q_sw = [True] * ((2 * n) - 1) #置けるクイーンの／方向

def set_queen(row, col):
    global q_pos, q_row, q_se, q_sw

    q_pos[col] = row #クイーンをおく
    q_row[row] = False #row列をおけないようにする
    q_se[col - row + N - 1] = False #左下からi番目の＼をおけないようにする
    q_sw[col + row] = False #左上からi番目の／を置けないようにする

def rm_queen(row, col):
    global q_row, q_se, q_sw
    #バックトラック
    q_row[row] = True #row列をおけないようにする
    q_se[col - row + N - 1] = True #左下からi番目の＼をおけない様にする
    q_sw[col + row] = True #左上からi番目の／を置けないようにする

def try_queen_all(col):
    global number
    for row in range(N):
        # row行col列が他のクイーンの効き筋になっていなければ
        if q_row[row] and q_se[col - row + N - 1] and q_sw[col + row]:
            set_queen(row, col)    # クイーンを配置
            if(col < (N - 1)):
                # クイーンを配置していない列がある
                try_queen_all(col + 1)
            else:
                number += 1
                print_queen()
            rm_queen(row, col) #強制バックトラック

def print_queen():
    with open('ex10_2.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['解番号 {:d}'.format(number)])
        for i in range(N):
            row = ["Q" if i == q_pos[j] else "." for j in range(N)]
            # 第i行の盤面の状態を"Q"(クイーン)と"."(何もなし)で表したリストを作る
            writer.writerow(row)
        writer.writerow('')

def main():
    global N, number
    N = 8
    number = 0
    init_queen(N)
    try_queen_all(0)

main()
