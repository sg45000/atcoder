"""
どこに点があっても長方形を同じ面積で２分割できる

また点は長方形の中心に存在すれば、複数の直線で分割が可能
"""
W, H, x, y = list(map(int, input().split(" ")))

half_area = W * H / 2

way = 1 if W / 2 == x and H / 2 == y else 0
print(str(half_area) + " " + str(way))