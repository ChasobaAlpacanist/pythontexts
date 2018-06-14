# 得点が同じ場合には学籍番号順(昇順)に出力する
#
# 演習課題 2 のプログラムを、得点が同じ場合には学籍番号順 ( 昇順 ) に
# 出力されるように改良しなさい
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
    numbers = []
    scores = []
    compare_count = 0
    change_count = 0
    for i in range(number):
        numbers.append(data[i].split(',')[0])
        scores.append(data[i].split(',')[2])
    for j in range(number - 1):
        max_index = j
        for k in range(j + 1, number):
            compare_count += 1
            if(scores[max_index] < scores[k]):
                max_index = k
            elif(scores[max_index] == scores[k]):
                if(numbers[max_index] > numbers[k]):
                    max_index = k
        change_count += 1
        numbers[j],numbers[max_index] = numbers[max_index],numbers[j]
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
    with open(regex.sub('_4.csv', name), 'w', newline = '') as f:
        writer = csv.writer(f)
        for i in data:
            i = i.split(',')
            writer.writerow(i)

main()
