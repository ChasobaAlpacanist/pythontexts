# ソートアルゴリズムの処理時間の比較
#
# (1) 乱数を利用して 3桁、4 桁、5 桁分のデータファイルを作成する
# (2) 単純選択ソート、クイックソート、バブルソート、マージソートの関数において、
#     データ件数による 各ソートアルゴリズムの処理時間を検討しなさい。
#     比較回数、入れ替え回数、および処理時間をそれぞれ表示させ
#     データ件数 3 桁、4 桁、5 桁のデータファイルのそれぞれでためしなさい
#
import sys
import random
import time


def main():
    for i in range(3, 6):
        print(str(i) + '桁のデータファイル')
        random_nums = create_random_nums(i)

        data_1 = Data_by_simple_selection(random_nums)
        data_2 = Data_by_bubble_sort(random_nums)
        data_3 = Data_by_quick_sort(random_nums)
        data_4 = Data_by_merge_sort(random_nums)

        start_time = time.time()
        data_1.array = data_1.simple_selection(data_1.array)
        erapsed_time = time.time() - start_time
        data_1.print_counter()
        print('処理時間:' + str(time.time() - start_time) + 'sec')

        start_time = time.time()
        data_2.array = data_2.bubble_sort(data_2.array)
        data_2.print_counter()
        print('処理時間:' + str(time.time() - start_time) + 'sec')

        start_time = time.time()
        data_3.array = data_3.quick_sort(data_3.array)
        erapsed_time = time.time() - start_time
        data_3.print_counter()
        print('処理時間:' + str(time.time() - start_time) + 'sec')

        start_time = time.time()
        data_4.array = data_4.merge_sort(data_4.array)
        erapsed_time = time.time() - start_time
        data_4.print_counter()
        print('処理時間:' + str(time.time() - start_time) + 'sec')

def create_random_nums(n):
    nums = []
    for i in range(10 ** (n - 1)):
        nums.append(int(random.random() * (10 ** (n - 1))))
    return nums

class Data_by_simple_selection():
    def __init__(self, array):
        self.array = array
        self.compare_counter = 0
        self.change_counter = 0

    def simple_selection(self, array):
        number = len(array)
        nums = []
        for i in range(number):
            nums.append(array[i])
        for j in range(number - 1):
            max_index = j
            for k in range(j + 1, number):
                self.compare_counter += 1
                if(nums[max_index] < nums[k]):
                    max_index = k
            self.change_counter += 1
            nums[j],nums[max_index] = nums[max_index],nums[j]
            array[j],array[max_index] = array[max_index], array[j]
        return array

    def print_counter(self):
        print('単純選択ソート:')
        print('比較回数' + str(self.compare_counter) + '回')
        print('交換回数' + str(self.change_counter) + '回')
        return

class Data_by_bubble_sort():
    def __init__(self, array):
        self.array = array
        self.compare_counter = 0
        self.change_counter = 0

    def bubble_sort(self, array):
        number = len(array)
        for i in range(number):
            for j in range(number - (i + 1)):
                self.compare_counter += 1
                if(array[j] > array[j + 1]):
                    self.change_counter += 1
                    array[j],array[j + 1] = array[j + 1],array[j]
        return array

    def print_counter(self):
        print('バブルソート:')
        print('比較回数' + str(self.compare_counter) + '回')
        print('交換回数' + str(self.change_counter) + '回')
        return

class Data_by_quick_sort():
    def __init__(self, array):
        self.array = array
        self.compare_counter = 0
        self.change_counter = 0

    def quick_sort(self, array):
        if(len(array) <= 1):
            return array
        else:
            pivot = array[len(array) // 2]
            left = []
            right = []
            for i in range(1, len(array)):
                self.compare_counter += 1
                if(array[i] < pivot):
                    self.change_counter += 1
                    left.append(array[i])
                else:
                    right.append(array[i])
            left = self.quick_sort(left)
            right = self.quick_sort(right)
            pivot = [array[0]]
            return(left + pivot + right)

    def print_counter(self):
        print('クイックソート:')
        print('比較回数' + str(self.compare_counter) + '回')
        print('交換回数' + str(self.change_counter) + '回')
        return

class Data_by_merge_sort():
    def __init__(self, array):
        self.array = array
        self.compare_counter = 0
        self.change_counter = 0

    def merge_sort(self, array):
        if(len(array) == 1):
            return array
        else:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            left = self.merge_sort(left)
            right = self.merge_sort(right)
            return self.merge_sort_merge(left, right)

    def merge_sort_merge(self, left, right):
        sorted_data = []
        left_index = 0
        right_index = 0
        while(left_index < len(left) and right_index < len(right)):
            self.compare_counter += 1
            self.change_counter += 1
            if(left[left_index] <= right[right_index]):
                sorted_data.append(left[left_index])
                left_index += 1
            else:
                sorted_data.append(right[right_index])
                right_index += 1
        if(left_index < len(left)):
            sorted_data.extend(left[left_index:])
        else:
            sorted_data.extend(right[right_index:])
        return sorted_data

    def print_counter(self):
        print('マージソート:')
        print('比較回数' + str(self.compare_counter) + '回')
        print('交換回数' + str(self.change_counter) + '回')
        return

sys.setrecursionlimit(100000000)
main()
