# 演習課題 4.
# Python のソースプログラムからコメントを除去するプログラムを作成しなさい

import re
import sys

def pop_comment(source):
    f = open(source, 'r')
    lines = f.readlines()
    f.close()
    s = open(source, 'w')
    regex = re.compile(r'#[^\n]*')
    for line in lines:
        s.write(regex.sub('', line))
    s.close()

def main():
    arg = sys.argv
    pop_comment(arg[1])

main()
