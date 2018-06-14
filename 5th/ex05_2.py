# 0～9の任意の整数をキーボードから EOF が入力されるまでリストに格納する。
# リストに 0～9 の値がそれぞれ何個あったかを数える関数 count を作成し
# メインプログラムで数えた結果を表示するプログラムを作成しなさい

def count_num(nums, x):
    counter = 0
    for i in range(len(nums)):
        if(x == nums[i]):
            counter += 1
        else: pass
    return (str(x) + 'は' + str(counter) + '個')

def main():
    nums = []
    try:
        print('0～9 の任意の整数を入力してください ( 入力終了は Ctrl-D ) :')
        num = input()
    except EOFError:
        pass
    else:
        try:
            while(True):
                nums.append(int(num))
                num = input()
        except EOFError:
            pass
    for i in range(10):
        print(count_num(nums, i))
    return

main()
