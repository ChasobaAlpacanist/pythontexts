# 演習課題 1.
#  ファイルからデータを読み込みながら登録番号をキーとした 探索木を作成しなさい。
#  また、木全体を表示する関数を作成し、出力例の様に木の構造が分かり
#  やすいように表示しなさい。
#
#  構造体の各メンバのデータ型は以下のようにすること
#
#     登録番号:     整数型
#     氏名:         文字列
#     プロフィール: 文字列
#
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

def create_tree(root, data):
    new_node_num = int(data.split()[0])
    if(root is None):
        root = Tree(data)
    elif(root.num > new_node_num):
        root.left = create_tree(root.left, data)
    else:
        root.right = create_tree(root.right, data)
    return root

main()
