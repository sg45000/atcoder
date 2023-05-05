def main(h, w, k, rows):
    answer = 0
    for bit in range(2 ** (h + w)):
        cp_rows = [[*row] for row in rows]
        for current_bit in range(h + w):
            if bit >> current_bit & 1:
                if current_bit < h:
                    cp_rows[current_bit] = ['R'] * w
                else:
                    for row in cp_rows:
                        row[current_bit - h] = 'R'
        count = 0
        for row in cp_rows:
            for tile in row:
                if tile == "#":
                    count += 1
        if count == k:
            answer += 1
    return answer
                

h, w, k = list(map(int, input().split(' ')))
rows = [list(input()) for _ in range(h)]
print(main(h, w, k, rows))