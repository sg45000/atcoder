N, Q = list(map(int, input().split(" ")))

train = [(-1,-1)] * (N + 1)

for _ in range(Q):
    query = list(map(int, input().split(" ")))
    if query[0] == 1:
        _, x, y = query
        train[x] = (train[x][0], y)
        train[y] = (x, train[y][1])
        
    elif query[0] == 2:
        _, x, y = query
        train[x] = (train[x][0], -1)
        train[y] = (-1, train[y][1])
    else:
        _, x = query

        i = x
        while train[i][0] > 0:
            i = train[i][0]
        
        count = 1
        train_nums = [i]
        while train[i][1] > 0:
            count += 1
            train_nums.append(train[i][1])
            i = train[i][1]
        print(count, *train_nums)