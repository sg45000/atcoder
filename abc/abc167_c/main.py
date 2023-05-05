def main(n, m, x, books):
    min_price = float('inf')
    for bit in range(2**n):  # 全組み合わせ数は 2のN乗
        total_price = 0
        total_exps = [0] * m
        for currentBit in range(n):  # currentBitは探索するビット番号
            if (bit >> currentBit & 1):  # 探索したいビットを１桁目にシフトして　1か確認。
                price, *exps = books[currentBit]  # ビットが立っていた場合は、そのビットの参考書を計算に入れる
                total_price += price
                total_exps = [x + y for (x, y) in zip(total_exps, exps)]
        if all([exp >= x for exp in total_exps]):  # 全てのアルゴリズムの理解度がx以上ならmin_priceの候補に入れる
            min_price = min(min_price, total_price)
    if min_price == float('inf'):
        return -1
    else:
        return min_price


n, m, x = list(map(int, input().split(' ')))
books = [list(map(int, input().split(' '))) for _ in range(n)]
print(main(n, m, x, books))
