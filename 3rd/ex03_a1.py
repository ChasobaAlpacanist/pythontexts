# 関数 max(int x, int y)は変数xと変数yを比較し、その大きなほうの値を得る
# 関数である。
# つぎの 3つの要件を満たす方法で、それぞれに関する関数を定義し
# それらを呼び出して結果を表示するプログラムを作りなさい。
# ( 全部で 3つの関数を定義する )
# 
# 要件(1) if文と else 節を使う
# 要件(2) if 文は使うが、else 節は使わない
# 要件(3) if 文は使わない

#(1)
def max1(x, y):
  if(x >= y):
    print(x)
    return
  else:
    print(y)
    return

#(2)
def max2(x, y):
  if(x >= y):
    print(x)
    return
  print(y)
  return

#(3)
def max3(x, y):
  nums = [x, y]
  nums.sort()
  print(nums[1])
  return

x = int(input('x?:'))
y = int(input('y?:'))
max1(x, y)
max2(x, y)
max3(x, y)

