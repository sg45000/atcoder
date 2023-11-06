"""
3面サイコロが3個あると仮定するとそれぞれの出目の積の総和は
x1y1z1 + x1y1z2 + x1y1z3 + x1y2z1 + x1y2z2 + ...
式変形すると
x1(y1(z1 + z2 + z3) + y2(z1 + z2 + z3) ...) + x2(y1(z1 + z2 + z3) + y2(z1 + z2 + z3) ...) ...
z1 + z2 + z3 = Z と置くと
x1(y1・Z + y2・Z + y3・Z) + x2(y1・Z + y2・Z + y3・Z) ...
となる
y1・Z + y2・Z + y3・Z = Z(y1 + y2 + y3) なので同様にy1 + y2 + y3をYと置くと
x1(YZ) + x2(YZ) + x3(YZ) となり式変形すると
YZ(x1 + x2 + x3) = XYZ となる
つまり、それぞれのサイコロの目の合計を掛け合わせれば答えが求まる
"""

N = int(input())

ans = 1
for _ in range(N):
    A = list(map(int, input().split()))
    ans *= sum(A) 
    ans %= (10 ** 9 + 7)

print(ans)