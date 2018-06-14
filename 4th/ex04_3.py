# 任意の整数を3桁ごとに「,」で区切って表示する関数を作成しなさい。
# 例えば、1000000は「1,000,000」と表示する。
#
# ただし、以下の再帰アルゴリズムを用いること。
#
# 例えば、もしnが3桁以下ならば、ただそれを表示する。
# そうでなければ、
# n/1000を再帰呼び出し(上位桁を表示)してから、「,」と下3桁(n%1000) を表示する。

def putting_comma(n):
    if(int(n / 1000) < 1):
        return str(n)
    else:
        return putting_comma(int(n / 1000)) + ',' + '{0:03d}'.format(n % 1000)
n = int(input('Integer?:'))
print(putting_comma(n))
