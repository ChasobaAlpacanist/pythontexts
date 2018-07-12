# 大きさの異なる A リットルのバケツと B リットルの空のバケツがあるとき、
# この 2つのバケツを使い C リットルの水を計量する手順を示すプログラムを
# 作成しなさい
#

class Bucket():
    def __init__(self, max_volume):
        self.MAX_VOLUME = max_volume
        self.now_volume = 0

    def drop(self):
        self.now_volume = 0

    def fill(self):
        self.now_volume = self.MAX_VOLUME

def move(from_bucket, to_bucket):
    #余るとき
    if(from_bucket.now_volume >= to_bucket.MAX_VOLUME - to_bucket.now_volume):
        from_bucket.now_volume -= (to_bucket.MAX_VOLUME - to_bucket.now_volume)
        to_bucket.now_volume = to_bucket.MAX_VOLUME
    #余らないとき
    else:
        to_bucket.now_volume += from_bucket.now_volume
        from_bucket.now_volume = 0

def try_action(actions, a, b, c):
    #a, bともに空の時、どちらかに水を入れる。
    if(a.now_volume = 0 and b.now_volume = 0):
        #Aに水を入れる
        a.fill()
        actions.append('Fill(a)')
        try_action(actions, a, b, c)
        #Bに水を入れる
        a.drop()
        actions.remove('Fill(a)')
        b.fill()
        actions.append('Fill(b)')
        try_action(actions, a, b, c)
    elif
