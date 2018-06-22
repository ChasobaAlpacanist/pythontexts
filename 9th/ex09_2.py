# 以下の関数を再帰を使って処理するプログラムを作成しなさい
#
# 関数 f( n ), g( n ) において
#
#    f( n ) = 1                            ( n ≦ 1 の時 )
#    f( n ) = n * g( n-1 )                 ( n ≦ 1 でない時 )
#    g( n ) = 0                            ( n = 0 の時 )
#    g( n ) = n + f( n-1 )                 ( n = 0 でない時 )
#
def f(n):
    if(n <= 1):
        return 1
    else:
        return n * (n - 1 + f(n - 2)) #g(n - 1)

def g(n):
    if(n == 0):
        return 0
    else:
        if(n - 1 <= 1):
            return n + 1
        else:
            return n + ((n - 1) * g(n - 2)) #f(n - 1)
def main():
    print('f(5) = ' + str(f(1)))
    print('g(5) = ' + str(g(1)))
    print('f(2) = ' + str(f(2)))
    print('g(2) = ' + str(g(2)))
    print('f(0) = ' + str(f(0)))
    print('g(0) = ' + str(g(0)))
    print('f(-1) = ' + str(f(3)))
    print('g(-1) = ' + str(g(3)))

main()
