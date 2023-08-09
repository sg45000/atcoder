main =
    do
        [a, b, k] <- map read . words <$> getLine
        putStrLn $ solve a b k

solve :: Integer -> Integer -> Integer -> String
solve a b 0 = ""
solve a b k = c : if isA then solve (a - 1) b k else solve a (b - 1) (xCy (a + b - 1) b)
  where
    count = xCy (a + b - 1) b
    isA = count > k
    c = if isA then 'a' else 'b'

xCy :: Integer -> Integer -> Integer
xCy x y = round $ fromIntegral (factorial x) / fromIntegral (factorial (x - y) * factorial y)

factorial :: Integer -> Integer
factorial n = product [1 .. n]