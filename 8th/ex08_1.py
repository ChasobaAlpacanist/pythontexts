# クイックソートによる整列
#
# 前回演習の演習課題1. で作成したプログラムを利用して
# 学生データの構造体配列とデータ件数を引数とし、得点を降順で整列する
# クイックソートのアルゴリズムを用いた整列関数を作成し、
# 整列した結果を表示するプログラムを作成しなさい。
#
import sys

def main():
    arg = sys.argv
    sorted_data = quick_sort(create_struct_array(arg[1]))
    for i in sorted_data:
        print(i)

def create_struct_array(data):
    student_data = []
    file = open(data, 'r')
    for student in file.readlines():
        student = student.split(' ')
        num = '{0:4d}'.format(int(student[0]))
        name = '{0:16s}'.format(student[1])
        score = '{0:3d}'.format(int(student[2]))
        student_data.append(num + ',' + name + ',' + score)
    file.close()
    return student_data

def quick_sort(array):
    if(len(array) <= 1):
        return array
    else:
        scores = []
        for i in array:
            scores.append(i.split(',')[2])
        pivot_index = len(array) // 2
        left = []
        right = []
        for i in range(0, len(array)):
            if(i != pivot_index):
                if(int(scores[i]) >= int(scores[pivot_index])):
                    left.append(array[i])
                else:
                    right.append(array[i])
        left = quick_sort(left)
        right = quick_sort(right)
        pivot = [array[pivot_index]]
        return(left + pivot + right)

main()
