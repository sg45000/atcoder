def main(n, m):
    scc = min(n, m // 2)     # 1. 与えられたsとcを組み合わせて、sccを作る。
    n = n - scc              # 2. 1でsccを作るために消費したsを引いておく
    m = (m - scc * 2)        # 3. 1でsccを作るために消費したsを引いておく
    if n == 0:
        return scc + m // 4  # 4. cのみで作ったsccを1で作ったsccと合わせて返す
    else:
        return scc  # 4. 1で作ったsccを返す


n, m = list(map(int, input().split(' ')))
print(main(n, m))