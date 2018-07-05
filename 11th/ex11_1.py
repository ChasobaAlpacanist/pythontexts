# １から９の整数から重複しない４つの数を選び、それらをa,b,c,dとした時、
#  ab , cd の組みをそれぞれ２桁の実数にして、ab を cd で割った時(ab/cd)、
#  ちょうど３となる ab , cd の組み合わせを全て表示しなさい

def find_pair():
    nums = list(range(1, 10))
    correct_pairs = []
    for a in nums:
        nums_9 = list(nums)
        nums_9.remove(a)
        for b in nums_9:
            nums_8 = list(nums_9)
            nums_8.remove(b)
            for c in nums_8:
                nums_7 = list(nums_8)
                nums_7.remove(c)
                for d in nums_7:
                    if((a * 10 + b) / (10 * c + d) == 3):
                        correct_pair = str(10 * a + b) + ', ' + str(10 * c + d)
                        correct_pairs.append(correct_pair)
    return correct_pairs

def main():
    print('ちょうど3になる組み合わせは以下')
    for i in find_pair():
        print(i)

main()
