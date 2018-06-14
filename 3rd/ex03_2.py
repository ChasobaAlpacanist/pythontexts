# 演習課題 1 のプログラムを次のように改変しなさい。
#
# main() 関数においては、
# ・入力された n が 負でない間は、関数で 2 乗和を計算し計算結果を出力するよう
#   ループを形成する。
# ・n に負の値が入力されたらプログラムを終了する。
#
# 2乗和の計算を計算する関数においては、
# ・最後に呼ばれた際の引数と戻り値を記憶しておく
# ・新たに呼び出されたとき、直前の呼び出しと引数の値が同じ場合、計算をせずに記憶しておいた値を戻り値とする
# ・再計算の必要があったかどうかを関数内でメッセージとして出力しなさい。

def main():
  sqsum = Squaresum()
  n = int(input('n?:'))
  while(n >= 0):
    print(sqsum.calculation(n))
    n = int(input('n?:'))
  print('Negative number')

class Squaresum:
  def __init__(self):
    self.num = 0
    self.total = 0

  def calculation(self,n):
    if(n == self.num):
      print('Not need for calculation')
      return(self.total)
    else:
      self.num = n
      self.total = 0
      while(n >= 1):
        self.total = self.total + n*n
        n = n - 1
      return self.total
main()
