# ５つの地点０～４を結ぶ道路網が図のようにある。
# 始点を０とし終点を４とした時、０から４に至る経路をすべて求めなさい。
# ただし、同じ地点を２度通ってはいけない
#

class Point():
    def __init__(self, name, nearby):
        #地点名と隣接地点の定義
        self.name = name
        self.nearby = nearby

def main():
    #地点情報の登録。routesは条件に合致した経路
    try_move(point_0, [point_0])
    for i in routes:
        i = list(map(lambda point:str(point.name), i))
        print(' '.join(i))

#引数iは現在地、routeは現在地を含む移動行程
def try_move(now_location, route):
    #隣接地点に行こうとする
    global routes
    for next_point in now_location.nearby:
        #行ったことのない経路の場合、移動する
        if(not(points[next_point] in route)):
            now_location = points[next_point]
            route.append(now_location)
            #移動先が4の時、経路をroutesに追加
            if(next_point == 4):
                route_pattern = list(route)
                routes.append(route_pattern)
            #移動先が4でない時、次の移動をする
            else:
                try_move(now_location, route)
            #バックトラック
            route.remove(now_location)

point_0 = Point(0, [1, 2])
points = [point_0, Point(1, [0, 2, 3, 4]), Point(2, [0, 1, 3]),
                Point(3, [0, 1, 4]), Point(4, [1, 3])]
routes = []
main()
