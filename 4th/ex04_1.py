# 前回の演習で定義した3次元ベクトルのタプルを用い、このタプルを引数として
# 外積を返す関数を作成し、利用するプログラムを作成しなさい

class Vector():
    def __init__(self):
        self.name = input('Name of vector?:')
        self.x = int(input('x for ' + self.name + '?:'))
        self.y = int(input('y for ' + self.name + '?:'))
        self.z = int(input('z for ' + self.name + '?:'))
        self.vector = (self.x, self.y, self.z)

def main():
    vector1 = Vector()
    vector2 = Vector()
    return print(outer_product(vector1.vector, vector2.vector))

def outer_product(v1, v2):
    x = (v1[1] * v2[2]) - (v1[2] * v2[1])
    y = (v1[2] * v2[0]) - (v1[0] * v2[2])
    z = (v1[0] * v2[1]) - (v1[1] * v2[0])
    return (x, y, z)
main()
