# ソート範囲を指定した条件付きバブルソート
#
# 正の整数が並んだ配列 a[] をバブルソートでソートするプログラムを作成しなさい
#
# ただし、ユーザが開始位置 m および終了位置 n ( 0 ≦ m ＜ n ≦ 配列の要素数 ) の
# 2 つの値を 設定できることとし、開始位置から終了位置までの要素のみをソートし、
# 結果の表示は配列の全要素を表示するものとする
#
# 例: a = [ 9, 1, 3, 7, 0, 5, 4, 2, 8, 6 ]
#
# m = 0, n = 9 の場合:
#     0 1 2 3 4 5 6 7 8 9
#
# m = 2, n = 7 の場合:
#     9 1 0 2 3 4 5 7 8 6
#
def main():
    a = [9,1,3,7,0,5,4,2,8,6]
    m = int(input('開始位置を入力:'))
    n = int(input('終了位置を入力:'))
    a = bubble_sort(a, m, n)
    for i in a:
        print(i, end = ' ')
    print('')

def bubble_sort(data, m, n):
    for i in range(n - m):
        for j in range(m, n - i):
            if(data[j] > data[j + 1]):
                data[j],data[j + 1] = data[j + 1],data[j]
    return data

main()
