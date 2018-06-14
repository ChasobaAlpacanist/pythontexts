# 整数型配列にデータが初期値で与えられている時、
# リストを引数としてリスト内の最大値を戻り値とする関数を作成し、
# メインプログラムでその値を出力するプログラムを作成しなさい

def return_max(nums):
    nums.sort()
    nums.reverse()
    return nums[0]

def main():
    nums = [2,53,442,33432,12,21,3,4,5555,6454]
    print('x[] = ' + str(nums)
    print('最大値 = ' + str(return_max(nums)))

main()
