# 整列過程におけるデータの比較回数とデータの入れ換え回数を表示し、
# 整列データをファイルに書き込む
#
# 演習課題 1 のプログラムを以下のように改良しなさい
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

def main():
    arg = sys.argv
    data = Data(arg[1])
    data.array = data.quick_sort(data.array)
    print('比較回数は:' + str(data.compare_counter) + '回')
    print('交換回数は:' + str(data.change_counter) + '回')
    data_writer(data.array, arg[2])

class Data():
    def __init__(self, array):
        self.array = self.create_struct_array(array)
        self.compare_counter = 0
        self.change_counter = 0

    def create_struct_array(self, data):
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

    def quick_sort(self, array):
        if(len(array) <= 1):
            return array
        else:
            scores = []
            for i in array:
                scores.append(i.split(',')[2])
            pivot_index = len(array) // 2
            left = []
            right = []
            for i in range(len(array)):
                if(i != pivot_index):
                    self.compare_counter += 1
                    if(int(scores[i]) >= int(scores[pivot_index])):
                        self.change_counter += 1
                        left.append(array[i])
                    else:
                        right.append(array[i])
            left = self.quick_sort(left)
            right = self.quick_sort(right)
            pivot = [array[pivot_index]]
            return(left + pivot + right)

def data_writer(data, name):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        for i in data:
            writer.writerow(i.split(','))

main()
