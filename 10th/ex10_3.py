# 以下の条件を満たす中で、価値の総和が最大になる組み合わせを全て求めて
# 表示するプログラムを作成しなさい
# 条件
# (1) 旅行かばんには持ち歩ける重量がある
#     ( 重量はその都度、キーボードから入力できるようにする )
# (2) 個々の品物には以下のような重さと価値 ( 重要度 ) が存在する
#       品名, 重さ, 価値 ( 重要度 )
#       本, 500g, 10点
#       傘, 500g, 90点
#       下着, 300g, 90点
#       上着, 1000g, 30点
#       薬, 20g, 100点
#       スマホ, 400g, 90点
#       パンフ, 200g, 10点
#       宿泊チケット, 10g, 100点
#       航空券, 10g, 100点
#       洗面用具本, 300g, 50点
#

import copy

def main():
    global limw, items, N, sel, optsel, maxv
    limw = int(input('重量制限を設定:'))
    items = [Item('本', 500, 10), Item('傘', 500, 90), Item('下着', 300, 90),
            Item('上着', 1000, 30), Item('薬', 20, 100), Item('スマホ', 400, 90),
            Item('パンフ', 200, 10), Item('宿泊チケット', 10, 100),
            Item('航空券', 10, 100), Item('洗面用具', 300, 50)]
    N = len(items)
    total_value = sum([i.value for i in items])
    sel = [False] * N #持っていくものリスト
    optsel = [False] * N #もっとも価値の高くなる可能性のある持ち物リスト
    maxv = 0 #optselの価値

    try_item(0, 0, total_value)

    print("重量制限 {:4d}gの場合: 総価値 {:3d}: ".format(limw, maxv), end="")
    sel_names = []
    for it,s in zip(items,optsel):
        if s:
            sel_names.append(it.name)
    print(" ".join(sel_names))    # " "を挟んで結合して表示

class Item():
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def try_item(i, now_weight, ex_value):
    global sel, optsel, maxv

    #i番目のものを入れようとする
    if(now_weight + items[i].weight <= limw): #制限以内
        sel[i] = True
        if(i < N - 1): #まだ考慮していないものがある
            try_item(i + 1, now_weight + items[i].weight, ex_value)
        elif(ex_value > maxv):
            maxv = ex_value
            optsel = copy.copy(sel)
        sel[i] = False #バックトラック

    #i番目を抜く
    ex_value1 = ex_value - items[i].value
    if(ex_value1 > maxv): #最大値を超える見込みあり
        if(i < N - 1):
            try_item(i + 1, now_weight, ex_value1)
        else:
            maxv = ex_value1
            optsel = copy.copy(sel)

main()
