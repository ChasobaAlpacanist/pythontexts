# 演習課題 4 のプログラムを改変して、第 3 回演習の課題 3 を参考にして２つの
# ベクトルの角度φを求めるプログラムに変更しなさい。
# 但し、ベクトルの大きさは演習課題４作成した内積を求める関数のどちらかを利用し、
# 新たに作成しないよう工夫すること

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

    def vector_magnitude(self):
      self.square_magnitude = 0
      for i in range(self.dimentions):
          self.square_magnitude += self.vector[i]**2
      magnitude = math.sqrt(self.square_magnitude)
      return magnitude

def inner_product(vector1, vector2):
    product = 0
    for i in range(vector1.dimentions):
        product += vector1.vector[i]*vector2.vector[i]
    return product

def angle(vector1, vector2):
    cosine = inner_product(vector1, vector2) / (vector1.vector_magnitude() * vector2.vector_magnitude())
    return math.degrees(math.acos(cosine))

def main():
    n = int(input('Dimentions?:'))
    vector1 = Vector(n, 'vector1')
    vector2 = Vector(n, 'vector2')
    print(angle(vector1, vector2))
    return

main()
