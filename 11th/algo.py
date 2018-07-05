class Tree:
    def __init__(self, key:int, count:int, left=None, right=None):
        self.key = key
        self.count = count
        self.left = left
        self.right = right

    # 木をprintする
    def print_tree(self, h=0):
        if self.right is not None:
            self.right.print_tree(h+1)    # 右部分木（あれば）をprint
        print("\t"*h, end="")    # 木の深さの分だけTAB(8文字字下げ)をprint (最後に改行しない)
        print("<{:d},{:d}>".format(self.key, self.count))    # その節点のキーと出現回数をprint
        if self.left is not None:
            self.left.print_tree(h+1)    # 左部分木（あれば）をprint

def search(x:int, t:Tree) -> Tree:
    if t is None:
        # Noneならば見つからなかったことになるので，新しく節点を生成する
        t = Tree(x, 1)
    elif x < t.key:
        t.left = search(x, t.left)
        # 現在の節点のキーよりも小さいので左部分木を探索
    elif x > t.key:
        t.right = search(x, t.right)
        # 現在の節点のキーよりも大きいので右部分木を探索
    else:
        t.count += 1

    return t

def del_tree(dstt:Tree, t:Tree) -> Tree:
    if t.right is not None:
        t.right = del_tree(dstt, t.right)
        # 最右節点でなければ右部分木を調べる
    else:
        # 最右節点の場合
        dstt.key = t.key
        dstt.count = t.count
        # 削除すべき節点にこの節点の内容をコピー
        t = t.left
        # 左部分木の繰り上げ

    return t

def delete(x:int, t:Tree) -> Tree:
    if t is None:
        # Noneなら見つからなかったことになる
        print("キー<{:d}>は見つかりませんでした。".format(x))
    elif x < t.key:
        t.left = delete(x, t.left)
        # 現在の節点のキーよりも小さいので左部分木を探索
    elif x > t.key:
        t.right = delete(x, t.right)
        # 現在の節点のキーよりも大きいので右部分木を探索
    else:
        # 見つかったので，この木の根を削除する
        print("キー<{:d}>が見つかりました。削除します。".format(x))
        if t.right is None:
            t = t.left
            # 左部分木だけなら，この木自身を左部分木に置き換える
        elif t.left is None:
            t = t.right
            # 右部分木だけなら，この木自身を右部分木に置き換える
        else:
            t.left = del_tree(t, t.left)
            # 左部分木の最右節点をこの木の根に移動する

    return t

# 初期データリスト
data = [8, 5, 10, 6, 9, 1, 12, 2, 4]

root = None
for d in data:
    root = search(d, root)
    """
    dをキーにもつ節点を木rootの中において探索/挿入する
    search()の中で木が新しく生成され，木の根が変化するので，新しい木の根を関数の値として返し，その値をrootに代入する
    """

print("最初の木構造：")
root.print_tree()
