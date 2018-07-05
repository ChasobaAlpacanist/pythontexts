# ある国の硬貨は 4種類あり、 A, B, C, 1 ( A > B > C > 1 ) の価値を持つとき、
# この硬貨を用いて、効果を組み合わせた合計金額が x となる最小枚数を求めよ
#

#変数min_coinsは最小枚数, min_pairは最小の組み合わせ
min_coins = 0

class Coin():
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #numberは使用した枚数
        self.number = 0
        self.min_num = 0

def main():
    A = Coin('A', int(input('硬貨Aの価値:')))
    B = Coin('B', int(input('硬貨Bの価値:')))
    C = Coin('C', int(input('硬貨Cの価値:')))
    Coin_1 = Coin(1, 1)
    x = int(input('合計金額:'))
    coins = [A, B, C, Coin_1]
    try_min_coin(x, 0, 0, coins)
    print(min_coins)
    print(min_pair)

    coin_nums = []
    for i in [A, B, C]:
        print(i.name + ' = ' + str(i.value) + '円')

    for j in range(len(coins)):
        formatted_data = '({:d}円, {:d}枚)'.format(coins[j].value, min_pair[j])
        coin_nums.append(formatted_data)

    print('以上の条件で' + str(x) + '円は')
    print(''.join(coin_nums) + 'で合計 ' + str(min_coins) + '枚。')

#変数now_coinsは現在の枚数
def try_min_coin(x, now_coins, value, coins):
    global min_coins
    #加えられるか確認
    for coin in coins:
        #合計金額がちょうどxか
        if(value + coin.value <= x):
            value += coin.value
            coin.number += 1
            now_coins += 1
            #ちょうど合計金額がxで最小枚数を更新しているか確認
            if(value == x):
                if(min_coins == 0 or now_coins < min_coins):
                    min_coins = now_coins
                    

            #合計金額がxを下回り、かつ使用枚数が最小枚数を超えていないか
            elif(now_coins < min_coins):
                try_min_coin(x, now_coins, value, coins)
        #加える時にはバックトラック
        value -= coin.value
        coin.number -= 1
        now_coins -= 1

main()
