# 二分探索
#
# 学生のデータを構造体の配列に読み込み、繰り返しで二分探索をするサーチ関数を
# 追加し、学籍番号を探索（ サーチ ）キーとする探索プログラムを作成しなさい。
#
# 対象となるファイルは学籍番号順（ 昇順 ）に整列されているものとする。
# 「 0 」あるいは負の学籍番号が入力されるまで、探索が繰り返し実行できるようする
#
import sys

def main():
    arg = sys.argv
    students_data = data_array(arg[1])
    sys.setrecursionlimit(10000)
    search_number(students_data)

def data_array(data):
    students_data = []
    file = open(data, 'r')
    for student in file.readlines():
        student = student.split(' ')
        students_data.append(student)
    file.close()
    return students_data

def search_number(array):
    numbers = []
    for student in array:
        numbers.append(int(student[0]))
    number = int(input('探索する学籍番号は？:'))
    while(number != 0):
        result = binary_search(numbers, number, 0, len(numbers) - 1)
        if (result == 'None'):
            print('該当者なし')
        else:
            student_num = '{0:4d}'.format(int(array[result][0]))
            student_name = '{0:16s}'.format(array[result][1])
            student_score = '{0:4d}'.format(int(array[result][2]))
            print(student_num + ' ' + student_name + ' ' + student_score)
        number = int(input('探索する学籍番号は？:'))

def binary_search(array, num, low, high):
    mid = (high + low) // 2
    if (low > high):
        return 'None'
    elif (array[mid] == num):
        return mid
    elif (array[mid] < num):
        return binary_search(array, num, mid + 1, high)
    elif (array[mid] > num):
        return binary_search(array, num, low, high - 1)

main()
