# 応用課題 1.
# Python のソースプログラムからコメント部分のみを出力するプログラムを作成しなさい

import re
import sys

def print_comment(source):
    regex = re.compile(r'#[^\n]+')
    f = open(source, 'r')
    lines = f.readlines()
    for line in lines:
        match = regex.findall(line)
        if match:
            for i in match:
                print(i)

def main():
    arg = sys.argv
    print_comment(arg[1])

main()
