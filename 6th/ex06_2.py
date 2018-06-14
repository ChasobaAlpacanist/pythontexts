# 演習課題 2.
# Coll_of_ES.txt というファイルを copy1.txt というファイルにコピーする
# プログラムを作成しなさい
import os.path

if(os.path.exists('Coll_of_ES.txt') == False):
    print('コピー元が存在しません')
elif(os.path.exists('copy1.txt')):
    print('コピー先のファイルがすでに存在しています。')
else:
    f = open('Coll_of_ES.txt', 'r')
    copy = open('copy1.txt', 'w')
    for line in f.readlines():
        copy.write(line)
    f.close()
    copy.close()
    print('ファイル Coll_of_ES.txt をファイル copy1.txt にコピーしました')
