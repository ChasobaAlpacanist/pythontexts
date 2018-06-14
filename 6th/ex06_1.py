# 演習課題 1.
# キーボードから入力した任意の複数行の文字列を読み込み、各行頭に行番号を付けて
# 標準出力に出力するプログラムを作成しなさい

import sys

def put_number(): #行の途中のサンプルコメント
    lines = []
    print('入力：')
    while(True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    print('入力された各行は以下の通り:')
    for i in range(len(lines)):
        print(str(i + 1) + ' ' + str(lines[i]))

def main():
    put_number()

main()
#行の末尾のサンプルコメント
