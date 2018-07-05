# 大きさの異なる A リットルのバケツと B リットルの空のバケツがあるとき、
# この 2つのバケツを使い C リットルの水を計量する手順を示すプログラムを
# 作成しなさい
#

def bukket_cal(a, b, c):
    #大きいバケツを整数回使ったのち、残りの水が小さいバケツの整数倍になれば手順を示す。
    bigger = max(a, b)
    smaller = max(a, b)
    i = 0
    while(bigger * i > c):
        water_left = c - bigger * i
        if(water_left % smaller == 0):
            
        i += 1
