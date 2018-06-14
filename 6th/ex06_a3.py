# 応用課題 3.
# 1000 回の正規疑似乱数の出力を csv ファイルに出力するプログラムを作成しなさい

import random
import csv
from decimal import Decimal, ROUND_HALF_UP

with open('normal_random.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for i in range(101): #0~100をとる。のちに i/100で0~1.00をとる。
        result = []
        num = Decimal(i * 0.01).quantize(Decimal('0.01'), rounding = ROUND_HALF_UP) #小数点2桁で統一
        result.append(str(num))
        for j in range(1, 10): #j個の和
            count = 0 #同じになった回数を数える
            for k in range(1000): #1000回の試行
                value = 0 #Σxの初期化
                for l in range(j):
                    value += random.random()
                normal_value = Decimal(value / j).quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)
                if(num.compare(normal_value) == Decimal('0')):
                    count += 1
            result.append(str(count))
        writer.writerow(result)
