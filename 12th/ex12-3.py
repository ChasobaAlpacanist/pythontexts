# 演習課題3
# 演習課題1 のプログラムに次の処理を追加しなさい。
#
# ・登録番号を入力するとその選手をリストから削除し、削除後のリストの内容を表示する
# ・該当者がいなければその旨を出力する
# ・登録番号に０が入力されるまで、繰り返し探索ができるようにする
#
# なお、削除の関数を定義すること
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
        if(delete_list(p, num)):
            print_list(p)
        num = int(input('登録番号を入力:'))
    print('終了します')

def print_list(p):
    while(p != None):
        print('<{:d}, {:s}, {:s}>'.format(p.number, p.name, p.profile))
        p = p.next
    print('')

def delete_list(p, number):
    while(p != None):
        if(p.number == number):
            #次が存在する時
            if(p.next != None):
                #pをqにすることでpは線形データから消える
                q = p.next
                p.key = q.key
                p.number = q.number
                p.name = q.name
                p.profile = q.profile
                p.next = q.next
                return True
            else:
                #pをNoneにする処理
                p_before.next = None
                return True
        else:
            p_before = p
            p = p.next
    print('該当者なし')
    return False

main()
