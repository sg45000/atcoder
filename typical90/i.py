import math


def calculate_angle(p1, p2, p3):
    """2次元座標上の3点を線で結んだ時の内角を計算する関数"""
    
    # p1を原点としたp2とp3のベクトルを計算
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])
    
    # 内積を計算
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    
    # 外積を計算
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]
    
    # atan2関数を使用して角度を計算
    angle = math.atan2(cross_product, dot_product)
    
    # ラジアンを度数に変換
    angle_degrees = math.degrees(angle)
    
    # 角度が負の場合は360度を加算して正の角度に変換
    if angle_degrees < 0:
        angle_degrees += 360
    
    return angle_degrees


N = int(input())
P = [list(map(int, input().split(" "))) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if j == k or i == k:
                continue
            angle = calculate_angle(P[i], P[j], P[k])
            if angle <= 180:
                answer = max(answer, angle)
print(answer)