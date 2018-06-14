# 2次元リストで 2x2 の正方行列を表現し、元のリストと逆行列用の
# リストを引数として逆行列を求める関数を作りなさい。
# 関数内で行列式を計算し、0 のときは逆行列が存在しないので、
# 関数を呼び出した側にそれがわかるように、逆行列を求める関数の
# 戻り値を行列式の値とすること。
# メインプログラムで結果#  ( 逆行列もしくは逆行列が存在しない
# ことの出力 ) で出力するプログラムを作成しなさい

def inverse_matrix(matrix):
    if(determinant(matrix) == 0):
        return 'Inverse Not Exist'
    else:
        inv_matrix = [[0,0],[0,0]]
        inv_matrix[0][0] = matrix[1][1] / determinant(matrix)
        inv_matrix[0][1] = -1 * matrix[0][1] / determinant(matrix)
        inv_matrix[1][0] = -1 * matrix[1][0] / determinant(matrix)
        inv_matrix[1][1] = matrix[0][0] / determinant(matrix)
        return inv_matrix

def determinant(matrix):
    return ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))

def input_matrix():
    matrix = [[], []]
    for i in range(2):
        for j in range(2):
            matrix[i].append(int(input(str(i + 1) + '行' + str(j + 1) + '列は?:')))
    return matrix

def main():
    print(inverse_matrix(input_matrix()))
    return

main()
