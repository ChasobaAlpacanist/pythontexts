# キーボードから入力した正数 n の階乗を求めるプログラムを
# 再帰を使う場合と、ループを使う場合それぞれ作成しなさい
#

#再帰
def factorial_recursion(n):
    if(n <= 1):
        return 1
    else:
        return n * factorial_recursion(n - 1)

#ループ
def factorial_roop(n):
    value = 1
    while(n >= 2):
        value *= n
        n -= 1
    return value

def main():
    n = int(input('n?:'))
    if(n < 0):
        print('負の値です。処理を中断します')
    else:
        print(factorial_recursion(n))
        print(factorial_roop(n))

main()
