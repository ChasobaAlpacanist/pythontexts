# 以下の関数を再帰を使って処理するプログラムを作成しなさい
#
# 関数 f( n, k ) において
#
#    f( n, k ) = 1                           ( k = 0 の時 )
#    f( n, k ) = f( n-1, k-1 ) + f(n-1, k)   ( 0 < k < n の時 )
#    f( n, k ) = 1                           ( k = n の時 )
#
def f(n, k):
    if(k == 0):
        return 1
    elif(k == n):
        return 1
    else:
        return f(n - 1, k - 1) + f(n - 1, k)

def main():
    n = int(input('n?:'))
    k = int(input('k?:'))
    print('f(n, k) = ' + str(f(n, k)))

main()
