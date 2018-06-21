# 正数 n のフィボナッチ数は以下の関数で求められる
#
# f( n ) = 0                     ( n = 0 の場合 )
# f( n ) = 1                     ( n = 1 の場合 )
# f( n ) = f( n-1 ) + f( n-2 )   ( n = 0 および n = 1 でない場合 )
#
# キーボードから入力した正数 n のフィボナッチ数を求めるプログラムを
# (a) 二重再帰を使う場合
# (b) 末尾再帰を使う場合
# (c) ループを使う場合
# それぞれ作成し、関数が呼び出された回数またはループが実行された回数を
# 表示し、比較、検討できるようにしなさい
#

#(a)
class Fibo():
    def __init__(self):
        self.counter = 0

    #(a)
    def fibo_a(self, n):
        self.counter += 1
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            return self.fibo_a(n - 1) + self.fibo_a(n - 2)

    #(b)
    def fibo_b(self, n, a = 1, b = 0):
        self.counter += 1
        if(n == 0):
            return 0
        elif(n == 1):
            return a
        else:
            return self.fibo_b(n - 1, a + b, a)

    #(c)
    def fibo_c(self, n):
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            i = 1
            value_a = 0
            value_b = 1
            while(i < n):
                self.counter += 1
                _value_a = value_a
                _value_b = value_b
                value_a = _value_b
                value_b = _value_a + _value_b
                i += 1
            return value_b

def main():
    fibonacci_a = Fibo()
    fibonacci_b = Fibo()
    fibonacci_c = Fibo()
    n = int(input('n?:'))

    print('二重再帰:')
    print('値は' + str(fibonacci_a.fibo_a(n)))
    print('呼び出し回数は' + str(fibonacci_a.counter) + '回')
    print('')

    print('末尾再帰:')
    print('値は' + str(fibonacci_b.fibo_b(n)))
    print('呼び出し回数は' + str(fibonacci_b.counter) + '回')
    print('')

    print('ループ:')
    print('値は' + str(fibonacci_c.fibo_c(n)))
    print('呼び出し回数は' + str(fibonacci_c.counter) + '回')

main()
