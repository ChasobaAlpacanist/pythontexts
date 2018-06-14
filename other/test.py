import math

x1 = int(input('x1?:'))
y1 = int(input('y1?:'))
z1 = int(input('z1?:'))
vector1 = (x1, y1, z1)

x2 = int(input('x2?:'))
y2 = int(input('y2?:'))
z2 = int(input('z2?:'))
vector2 = (x2, y2, z2)

def vector_magnitude(x, y, z):
  return math.sqrt(x*x + y*y + z*z)

def inner_product(vector1, vector2):
  product = 0
  for i in range(3):
    product = product + vector1[i]*vector2[i]
  return product

deg = math.acos(inner_product(vector1, vector2) /
             round((vector_magnitude(*vector1)*vector_magnitude(*vector2)), 10))
deg = math.degrees(deg)
print(vector_magnitude(*vector1))
print(vector_magnitude(*vector2))
print(inner_product(vector1, vector2))
print(inner_product(vector1, vector2) /
             (vector_magnitude(*vector1)*vector_magnitude(*vector2)))
print(deg)
