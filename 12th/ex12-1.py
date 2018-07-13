# 演習課題1
#  ファイルからデータを読み込みながら線形リストを生成し、
#  (新しいデータがリストの手前となる様にする)
#  リストの内容を手前から表示するプログラムを作成しなさい
#
#  構造体の各メンバのデータ型は以下のようにすること
#
#     登録番号:     整数型
#     氏名:         文字列
#     プロフィール: 文字列
#

import sys

class List():
    def __init__(self, data, next = None):
        split_data = data.split()
        self.number: int = int(split_data[0])
        self.name: str = split_data[1]
        self.profile: str = split_data[2]
        self.next = next

def main():
    args = sys.argv
    p = None
    with open(args[1], 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            newp = List(lines[i], p)
            p = newp
    print_list(p)

def print_list(p):
    while(p != None):
        print('{:d} {:s} {:s}'.format(p.number, p.name, p.profile))
        p = p.next
    print('')

main()
