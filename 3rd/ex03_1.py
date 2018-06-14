# 繰り返しを使って 1, 2, ..., n の 2 乗和 1^2 + 2^2 + ... + n^2 を計算しなさい。
# ただし，n の値は、input() で入力し、n = 10 の場合を提出すること。
# 2 乗和を求める部分は関数にし、引数 n を受け取ると2 乗和の計算結果を
# 戻り値とする関数にしなさい。

def squaresum(num):
    n = int(input('n?:'))
  if(num > 1):
    return num*num + squaresum(num - 1)
  else:
    return 1

print(squaresum(n))
