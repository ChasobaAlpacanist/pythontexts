# 2つの正の整数の最大公約数を、ユークリッドの互除法で、再帰を使って求めなさい
def euclidian(a, b):
    nums = [max(a,b), min(a,b)]
    if(nums[0] % nums[1] == 0):
        return nums[1]
    else:
        return euclidian(b, nums[0] % nums[1])

def main():
    a = int(input('a?:'))
    b = int(input('b?:'))
    return print(euclidian(a, b))

main()
