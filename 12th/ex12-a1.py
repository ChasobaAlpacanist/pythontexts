# 応用課題
# 演習課題1 のプログラムに次の処理を追加しなさい。
#
# ・ファイルからデータを読み込みながら登録番号順(昇順)にソートされたリストを
#   作成するようにし、リストの内容を表示しなさい。
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
        for line in lines:
            newp = List(line, None)
            if(p == None):
                p = newp
            else:
                sorted_list_by_number(newp, p)
    print_list(p)

def sorted_list_by_number(x, p):
    while(True):
        if(p.next == None):
            p.next = x
            break
        elif(p.number > x.number):
            tmp_data = ' '.join([str(x.number), x.name, x.profile])
            tmp = List(tmp_data)
            #xをpにする
            x.number = p.number
            x.name = p.name
            x.profile = p.profile
            x.next = p.next
            #pの情報をxにして後ろx(元はp)を繋げる
            p.number = tmp.number
            p.name = tmp.name
            p.profile = tmp.profile
            p.next = x
            break
        p = p.next


def print_list(p):
    while(p != None):
        print('<{:d}, {:s}, {:s}>'.format(p.number, p.name, p.profile))
        p = p.next
    print('')

main()
