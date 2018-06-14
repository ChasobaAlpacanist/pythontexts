# タプルで3次元ベクトルを表わし、2つのベクトルのなす角度φを求めなさい。
# その際、タプルを引数としてベクトルの大きさを求める関数と内積を求める関数を
# それぞれ別々に作成し、計算に用いなさい。
import math

class Vector():
    def __init__(self):
        self.name = input('Name of vector?:')
        self.x = float(input('x for ' + self.name + '?:'))
        self.y = float(input('y for ' + self.name + '?:'))
        self.z = float(input('z for ' + self.name + '?:'))
        self.vector = (self.x, self.y, self.z)

    def vector_magnitude(self):
      return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def inner_product(vector1, vector2):
  product = 0
  for i in range(3):
    product = product + vector1[i]*vector2[i]
  return product

def rad_to_deg(rad):
  return rad * 180 / math.pi

def main():
    vector1 = Vector()
    vector2 = Vector()
    rad = math.acos(inner_product(vector1.vector, vector2.vector) /
            round((vector1.vector_magnitude()*
                vector2.vector_magnitude()), 10))
    deg = round(rad_to_deg(rad), 8)
    print(str(deg) + ' degrees')
main()
