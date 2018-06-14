# 単純選択整列による整列
#
# 学生データの構造体配列とデータ件数を引数とし、得点を降順で整列する
# 単純選択整列のアルゴリズムを用いた整列関数を作成し、
# 整列した結果を表示するプログラムを作成しなさい。
#

import sys

def main():
    arg = sys.argv
    student_data = formatted_data(arg[1])
    print('ソート前')
    print_data(student_data)

    sorted_data = simple_selection(student_data, len(student_data))
    print('ソート後')
    print_data(sorted_data)

def simple_selection(data, number):
    scores = []
    for i in range(number):
        scores.append(data[i].split(',')[2])
    for j in range(number - 1):
        max_index = j
        for k in range(j + 1, number):
            if(scores[max_index] < scores[k]):
                max_index = k
        scores[j],scores[max_index] = scores[max_index],scores[j]
        data[j],data[max_index] = data[max_index], data[j]
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

main()
