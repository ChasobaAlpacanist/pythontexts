# 演習課題3
# 演習課題1 のプログラムに次の処理を追加しなさい。
#
# ・登録番号を入力するとその選手をリストから削除し、削除後のリストの内容を表示する
# ・該当者がいなければその旨を出力する
# ・登録番号に０が入力されるまで、繰り返し探索ができるようにする
#
# なお、削除の関数を定義すること
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
            newp = List(line, p)
            p = newp
    print_list(p)
    num = int(input('登録番号を入力:'))
    while(num != 0):
        delete_list(p, num)
        print_list(p)
        num = int(input('登録番号を入力:'))
    print('終了します')

def print_list(p):
    while(p != None):
        print('{:d}, {:s}, {:s}'.format(p.number, p.name, p.profile))
        p = p.next
    print('')

def delete_list(p, number):
    while(p != None):
        if(p.number == number):
            print('--削除しました--')
            #次が存在する時
            if(p.next != None):
                #pをqにすることでpは線形データから消える
                q = p.next
                p.number = q.number
                p.name = q.name
                p.profile = q.profile
                p.next = q.next
                return
            else:
                #pをNoneにする処理
                p_before.next = None
                return
        else:
            p_before = p
            p = p.next
    print('--該当者なし--')
    return
    
main()
