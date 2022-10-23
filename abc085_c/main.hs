main = do
    [n,y] <- map read . words <$> getLine
    let xs = [[a, b, c] | a <- [0..n], b <- [0..(n-a)], let c = n - a - b, a * 10000 + b * 5000 + c * 1000 == y]
    putStrLn $ unwords $ map show (if null xs then [-1, -1, -1] else head xs)