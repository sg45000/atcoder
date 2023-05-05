main = do
  n <- readLn
  [a, b, c] <- map read . words <$> getLine
  let result = [x + y + z | x <- [0 .. 9999], y <- [0 .. 9999], let z = (n - x * a - y * b) `div` c, 0 <= z, n == x * a + y * b + z * c]
  print $ minimum result