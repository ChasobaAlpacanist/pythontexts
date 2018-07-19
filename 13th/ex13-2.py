# 演習課題 2.
#  演習課題 1. のプログラムに次の処理を追加しなさい。
#
#  ・関数で木を作成後、以下のメニューを表示し、1, 2, 3 の入力することで
#    探索、削除、表示のいずれかを実行し、4 でプログラムを終了させるようにする
#  ・探索と削除の場合は、キーとなる登録番号を入力し、探索と削除の実行は
#    関数として作成しなさい
#  ・削除の場合、両枝にデータがある節のデータや最も根 ( root ) に近い
#    データなどが特殊なので特に確認しなさい

import sys

class Tree():
    def __init__(self, data):
        split_data = data.split()
        self.num: int = int(split_data[0])
        self.name: str = split_data[1]
        self.profile: str = split_data[2]
        self.right = None
        self.left = None

    def print_tree(self, depth = 0):
        if(self.right is not None):
            self.right.print_tree(depth + 1)
        print('\t' * depth, end = '')
        print('{:d} {:s} {:s}'.format(self.num, self.name, self.profile))
        if(self.left is not None):
            self.left.print_tree(depth + 1)

def main():
    args = sys.argv
    with open(args[1], 'r') as f:
        lines = f.readlines()
        root = None
        for line in lines:
            root = create_tree(root, line)
        root.print_tree()
        print('1:探索 2:削除 3:表示 4:終了')
        num = int(input('処理番号を入力:'))
        while(num != 4):
            if(num == 1):
                x = int(input('登録番号を入力:'))
                search_tree(root, x)
            elif(num == 2):
                x = int(input('登録番号を入力:'))
                root = delete_tree(root, x)
            elif(num == 3):
                root.print_tree()
            else:
                print('入力エラーです。もう一度入力してください。')
            num = int(input('処理番号を入力:'))
        print('終了します')

def create_tree(root, data):
    new_node_num = int(data.split()[0])
    if(root is None):
        root = Tree(data)
    elif(root.num > new_node_num):
        root.left = create_tree(root.left, data)
    else:
        root.right = create_tree(root.right, data)
    return root

def search_tree(root, x):
    if(root is None):
        print('存在しませんでした')
    elif(root.num > x):
        search_tree(root.left, x)
    elif(root.num < x):
        search_tree(root.right, x)
    else:
        print('{:d} {:s} {:s}'.format(root.num, root.name, root.profile))

def delete_tree(root, x):
    if(root is None):
        print('存在しませんでした')
    elif(root.num > x):
        root.left = delete_tree(root.left, x)
    elif(root.num < x):
        root.right = delete_tree(root.right, x)
    else:
        print('削除しました')
        if(root.right is None):
            root = root.left
        elif(root.left is None):
            root = root.right
        else:
            #左部分木の最大ノードを削除ノードと置き換える
            root.left = del_tree(root, root.left)
    return root

def del_tree(del_node, tree):
    if(tree.right is not None):
        tree.right = del_tree(del_node, tree.right)
    else:
        #削除ノードと左部分木最大ノードの値の入れ替え
        del_node.num = tree.num
        del_node.name = tree.name
        del_node.profile = tree.profile
        tree = tree.left
    return tree

main()
