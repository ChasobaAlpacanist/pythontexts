# 応用課題
# 演習課題1 のプログラムに次の処理を追加しなさい。
#
# ・ファイルからデータを読み込みながら登録番号順(昇順)にソートされたリストを
#   作成するようにし、リストの内容を表示しなさい。
#

class List():
    def __init__(self, key, data, next = None):
        self.key = key
        self.data = data
        self.next = next

def main():
    p = None
    with open('zac_japan.txt', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            newp = List(i, lines[i], None)
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
        elif(int(p.data.split()[0]) > int(x.data.split()[0])):
            tmp = List(x.key, x.data)
            #xをpにする
            x.key = p.key
            x.data = p.data
            x.next = p.next
            #pの情報をxにして後ろx(元はp)を繋げる
            p.key = tmp.key
            p.data = tmp.data
            p.next = x
            break
        p = p.next


def print_list(p):
    while(p != None):
        split_data = p.data.split()
        print('<{:d}, {:s}, {:s}>'.format(int(split_data[0]), split_data[1], split_data[2]))
        p = p.next
    print('')

main()
