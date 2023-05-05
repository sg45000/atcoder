-- 因数分解
-- O(sqrt(n))にしたい...
main = do
    n <- readLn :: IO Integer
    let a = (floor . sqrt . fromIntegral) n
    let b = [u | u <- [1 .. a], ((== 0) . mod n) u]
    print $ b ++ map (div n) b

gcd' a 0 = a
gcd' a b = gcd' b (a `mod` b)
