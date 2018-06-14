#演習課題３の関数を再帰を使わずに繰り返し(ループ)で作成しなさい。

#配列を宣言し、表示する下3桁(n%1000)の値またはnを配列に保存しておき、
#再帰の時と同じ手順で処理する。
def putting_comma(n):
    num = []
    while(n >= 1000):
        num.insert(0, '{0:03d}'.format(n % 1000))
        n = int(n / 1000)
    num.insert(0, str(n))
    return ','.join(num)

n = int(input('n?:'))
print(putting_comma(n))
