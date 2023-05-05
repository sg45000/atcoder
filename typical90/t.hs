main = do
    [a, b, c] <- map read . words <$> getLine
    putStrLn $ if a < pow c b then "Yes" else "No"

pow x 1 = x
pow x y = x * pow x (y - 1)