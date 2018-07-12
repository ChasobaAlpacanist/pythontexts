# 演習課題2
# 演習課題1 のプログラムに次の処理を追加しなさい。
#
# ・登録番号を入力するとその登録番号の選手を探索し、名前を出力する
# ・該当者がいなければその旨を出力する
# ・登録番号に０が入力されるまで、繰り返し探索ができるようにする
#
#  なお、探索は関数とすること
#

class List():
    def __init__(self, key, data, next = None):
        split_data = data.split()
        self.key = key
        self.number = int(split_data[0])
        self.name = split_data[1]
        self.profile = split_data[2]
        self.next = next

def main():
    p = None
    with open('zac_japan.txt', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            newp = List(i, lines[i], p)
            p = newp
    num = int(input('登録番号を入力:'))
    while(num != 0):
        print(search_list_name(p, num))
        num = int(input('登録番号を入力:'))
    print('終了します')

def print_list(p):
    while(p != None):
        print('<{:d}, {:s}, {:s}>'.format(p.number, p.name, p.profile))
        p = p.next
    print('')

def search_list_name(p, number):
    while(p != None):
        if(p.number == number):
            return p.name
        else:
            p = p.next
    return '該当者なし'

main()
