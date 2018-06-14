# リストでベクトルを表現し、その内積を求める関数を作りなさい。
# プログラムは以下の条件を満たすこと。
# (1) ベクトルの次数およびデータはキーボード入力とする
# (2) 内積を求める関数にはベクトルの次数を引数で渡し、任意の次元のベクトルを
#     扱うことができるようにすること
# (3) 関数の戻り値が内積の値となるようにすること
# (4) 内積を求める関数はリストの操作で内積を求めるように作成し、
#     メインプログラムから関数を呼び出すこと

import math

class Vector:
    def __init__(self, dimentions, name):
        self.name = name
        self.dimentions = dimentions
        self.vector = []
        for i in range(self.dimentions):
            self.value = float(input('Value of n' + str(i + 1) + ' for ' + self.name + '?:'))
            self.vector.append(self.value)
        return

def inner_product(dimentions):
    vector1 = Vector(dimentions, 'vector1')
    vector2 = Vector(dimentions, 'vector2')
    product = 0
    for i in range(dimentions):
        product += vector1.vector[i]*vector2.vector[i]
    return product

def main():
    n = int(input('Dimentions?:'))
    print(inner_product(n))

main()
