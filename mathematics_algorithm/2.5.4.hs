-- 素数判定
main = do
    n <- readLn
    print [u | u <- [2 .. n], let sr = (floor . sqrt . fromIntegral) u, all ((/= 0) . mod u) [2 .. sr]]

isPrime n
    | n <= 1 = False
    | n == 2 = True
    | even n = False
    | otherwise = go 3
  where
    go i
        | i * i > n = True
        | n `mod` i == 0 = False
        | otherwise = go (i + 2)