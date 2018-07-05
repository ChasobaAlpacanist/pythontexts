# 課題 3. の各地点間の距離全てが等距離であるとした場合、プログラムを
# 最短経路(通過する地点の一番少ないもの)を１つ求めるものに変更しなさい。
# 見つかった経路より短い経路が見つかる可能性がある場合のみ調べるように
# 効率化をはかりなさい
#

class Point():
    def __init__(self, name, nearby):
        #地点名と隣接地点の定義
        self.name = name
        self.nearby = nearby

def main():
    #地点情報の登録、shortest_routeは最小経路
    global shortest_route
    try_move(point_0, [point_0])
    shortest_route = list(map(lambda point:str(point.name), shortest_route))
    print(' '.join(shortest_route))

#引数iは現在地、routeは現在地を含む移動行程
def try_move(now_location, route):
    global shortest_route
    #隣接地点に行こうとする
    for next_point in now_location.nearby:
        #行ったことのない地点の場合、移動する
        if(not(points[next_point] in route)):
            now_location = points[next_point]
            route.append(now_location)
            #移動先が4の時、最短経路を更新
            if(next_point == 4):
                shortest_route = list(route)
            #移動先が4でなく、後の経路が暫定最小経路よりも短い場合、次の移動をする
            elif(shortest_route == [] or len(route) + 1 < len(shortest_route)):
                try_move(now_location, route)
            #バックトラック
            route.remove(now_location)

point_0 = Point(0, [1, 2])
points = [point_0, Point(1, [0, 2, 3, 4]), Point(2, [0, 1, 3]),
                Point(3, [0, 1, 4]), Point(4, [1, 3])]
shortest_route = []

main()
