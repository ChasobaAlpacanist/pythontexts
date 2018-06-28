# 5 x 5 のチェスの盤面の中央に「騎士 ( knight ) 」を置いた時、
# 全てのマス目をただ 1 度だけ訪問するすべての指し手を
# 表示するプログラムを作成しなさい
#
import csv

def main():
    global board, move_vec, number
    number = 0
    move_vec = [(2,1), (1,2), (-1,2), (2,-1), (-2,1), (1,-2), (-2,-1), (-1,-2)]

    board = []
    for i in range(5):
        board.append([0] * 5) #リストboardを初期化し、真ん中を1とする
    board[2][2] = 1
    try_move_all(2, 2, 2)

def move_to(i, y, x):
    global board
    board[y][x] = i

def undo(y, x):
    global board
    board[y][x] = 0

def try_move_all(i, y, x):
    global move_vec, number
    for dy, dx in move_vec:
        y1 = y + dy
        x1 = x + dx

        #動いた後の駒が盤面上にあるか、また行ったことのないマスか
        if(0 <= x1 < 5 and 0 <= y1 < 5 and board[y1][x1] == 0):
            #駒の移動を記録
            move_to(i, y1, x1)
            #まだ移動する余地があるか
            if(i < 25):
                try_move_all(i + 1, y1, x1)
            else:
                number += 1
                print_knights()
            undo(y1, x1)

def print_knights():
    with open('ex10_1.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['指し手 {:d}'.format(number)])
        for row in board:
            line = ['{:2d}'.format(a) for a in row]
            writer.writerow(line)
        writer.writerow('')

main()
