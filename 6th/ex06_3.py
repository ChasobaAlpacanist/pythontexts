# 演習課題 3.
# 2つのファイルが同一であるかを判定するプログラムを作成しなさい

import sys
def same_checker(file_one, file_two):
    fa = open(file_one, 'r')
    fb = open(file_two, 'r')
    if(fa.read() == fb.read()):
        print('同一')
    else:
        print('同一でない')
    fa.close()
    fb.close()

def main():
    arg = sys.argv
    same_checker(arg[1], arg[2])

main()
