# 応用課題 1.
#  任意の英文テキストのファイルを読み込み、出現する各単語の数をカウントする
#  プログラムを「2分探索木」を使用して作成しなさい
import sys

class WordTree():
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.right = None
        self.left = None

    def print_tree(self):
        if(self.right is not None):
            self.right.print_tree()
            print(self.word + ' -> ' + str(self.count) + '回')
        if(self.left is not None):
            self.left.print_tree()

def main():
    root = None
    args = sys.argv
    with open(args[1], 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            for word in line:
                #全ての文字を小文字とする。(単数と複数は別文字として区別される)
                small_word = word.lower()
                root = create_tree(root, small_word)
        root.print_tree()

def create_tree(root, word):
    if(root is None):
        root = WordTree(word)
    else:
        word_list = [root.word, word]
        word_list.sort()
        #前に文字列が存在した場合,countを1つ増やす
        if(root.word == word):
            root.count += 1
        #辞書順でwordの方が早い場合、右の枝におく
        elif(word_list[0] == word):
            root.right = create_tree(root.right, word)
        else:
            root.left = create_tree(root.left, word)
    return root

main()
