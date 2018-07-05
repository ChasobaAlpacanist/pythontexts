# 最大積載量１５トンのトラックが１台と、それぞれ７,４,５,６,３トンの
# 重さの荷物が１個ずつあります
# 最大積載量丁度で運べる荷物の組合せをすべて出力しなさい
#

items = [7, 4, 5, 6, 3]
item_names = {7: 'A', 4: 'B', 5: 'C', 6: 'D', 3: 'E'}
loads_patterns = []
loads = [] #積む荷物リスト

def main():
    put_test(0, 0, sum(items))
    for pattern in loads_patterns:
        load_content = map(lambda item:item_names[item], pattern)
        print(' '.join(list(load_content)))

def put_test(i, now_weight, total_weight):
    global loads_patterns, loads
    #i番目の荷物を積む
    if(now_weight + items[i] <= 15):
        loads.append(items[i])
        now_weight += items[i]
        if(now_weight == 15):
            correct_pattern = list(loads)
            loads_patterns.append(correct_pattern)
        #荷物の量が15トン未満で、かつまだ検討するものがある場合
        elif(i < len(items) - 1):
            put_test(i + 1, now_weight, total_weight)
        #バックトラック
        loads.remove(items[i])
        now_weight -= items[i]

    #i番目の荷物を積まない場合
    total_weight -= items[i]
    #候補の総重量が15トンを超えていて、かつまだ検討するものがある場合
    if(total_weight >= 15 and i < len(items) - 1):
        put_test(i + 1, now_weight, total_weight)

main()
