main = do
    [n, k] <- map read . words <$> getLine
    a <- map read . words <$> getLine
    b <- map read . words <$> getLine
    let diff = zipWith (\x y -> abs $ x - y) a b
    putStrLn $ if k - sum diff >= 0 && even (k - sum diff) then "Yes" else "No"