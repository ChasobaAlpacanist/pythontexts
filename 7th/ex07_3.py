# 整列過程におけるデータの比較回数とデータの入れ換え回数を表示し、
# 整列データをファイルに書き込む
#
# 演習課題 2 のプログラムを以下のように改良しなさい
#
# (1) 整列過程におけるデータの比較回数とデータの入れ換え回数を数え、
#     ディスプレイに出力する機能を追加する
#
# (2) データを表示する関数を、ファイルに出力する関数に変更し整列した
#     データをファイルに書き込みなさい
#     出力ファイル名もコマンド引数で指定すること。
#
import sys
import csv
import re

def main():
    arg = sys.argv
    student_data = formatted_data(arg[1])
    print('ソート前')
    print_data(student_data)

    sorted_data = simple_selection(student_data, len(student_data))
    print('ソート後')
    print_data(sorted_data)
    write_data(sorted_data, arg[1])

def simple_selection(data, number):
    scores = []
    compare_count = 0
    change_count = 0
    for i in range(number):
        scores.append(data[i].split(',')[2])
    for j in range(number - 1):
        max_index = j
        for k in range(j + 1, number):
            compare_count += 1
            if(scores[max_index] < scores[k]):
                max_index = k
        change_count += 1
        scores[j],scores[max_index] = scores[max_index],scores[j]
        data[j],data[max_index] = data[max_index], data[j]
    print('比較回数:' + str(compare_count))
    print('データ入れ替え回数:' + str(change_count))
    return data

def formatted_data(data):
    file = open(data, 'r')
    students_data = []
    for student in file.readlines():
        student = student.split(' ')
        num = '{0:4d}'.format(int(student[0]))
        name = '{0:16s}'.format(student[1])
        score = '{0:3d}'.format(int(student[2]))
        students_data.append(num + ',' + name + ',' + score)
    file.close()
    return students_data

def print_data(data):
    for student_data in data:
        print(student_data)

def write_data(data, name):
    regex = re.compile(r'\.txt$')
    with open(regex.sub('_3.csv', name), 'w', newline = '') as f:
        writer = csv.writer(f)
        for i in data:
            i = i.split(',')
            writer.writerow(i)

main()
