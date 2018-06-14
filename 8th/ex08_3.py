# 得点が同じ場合には学籍番号順(昇順)に出力する
#
# 演習課題 2 のプログラムを、得点が同じ場合には学籍番号順 ( 昇順 ) に
# 出力されるように改良しなさい
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
            numbers = []
            for i in array:
                scores.append(i.split(',')[2])
                numbers.append(i.split(',')[0])
            pivot_index = len(array) // 2
            left = []
            right = []
            for i in range(len(array)):
                if(i != pivot_index):
                    self.compare_counter += 1
                    if(int(scores[i]) > int(scores[pivot_index])):
                        self.compare_counter += 1
                        left.append(array[i])
                    elif(int(scores[i]) == int(scores[pivot_index])):
                        self.compare_counter += 1
                        if(int(numbers[i]) < int(numbers[pivot_index])):
                            self.change_counter += 1
                            left.append(array[i])
                        else:
                            self.change_counter += 1
                            right.append(array[i])
                    else:
                        self.change_counter += 1
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
