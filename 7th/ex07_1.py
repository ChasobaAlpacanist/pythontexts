# ファイルに格納されたデータを構造体の配列に格納し、表示する
#
# 指定された入力データのファイルから学生のデータを構造体の配列に読み込み、
# 全てのデータを整形して表示するプログラムを作成しなさい
#
# 1行の表示フォーマットは以下の通り
# 学生番号: 半角数字4文字分、区切り記号: 半角カンマ ( , )、
# 氏名: 半角文字列 16 文字分、区切り記号: 半角カンマ ( , )、
# 得点: 半角正数3文字分
#
import sys

def main():
    arg = sys.argv
    student_data = []
    file = open(arg[1], 'r')
    for student in file.readlines():
        student = student.split(' ')
        num = '{0:4d}'.format(int(student[0]))
        name = '{0:16s}'.format(student[1])
        score = '{0:3d}'.format(int(student[2]))
        student_data.append(num + ',' + name + ',' + score)
    file.close()
    for i in student_data:
        print(i)

main()
