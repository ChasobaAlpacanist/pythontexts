# 応用課題 2.
# ファイルの行数、文字数(バイト数)、単語数を数えるプログラムを作成しなさい

import re
import sys

def count_lines(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return len(lines)

def count_bytes(file):
    f = open(file, 'r')
    file_content = f.read()
    f.close()
    return len(file_content)

def count_words(file):
    regex = re.compile(r'\b\w+\b')
    f = open(file, 'r')
    file_content = f.read()
    words = regex.findall(file_content)
    f.close()
    return len(words)

def main():
    arg = sys.argv
    file = arg[1]
    print('行数は' + str(count_lines(file)))
    print('文字数は' + str(count_bytes(file)) + 'バイト')
    print('単語数は' + str(count_words(file)))

main()
