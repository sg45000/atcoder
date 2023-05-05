f :: Int -> Int
f x 
    | x `mod` 2 == 0 = 1 + f (x `div` 2)
    | otherwise = 0

main :: IO ()
main = do
  getLine
  xs <- map read . words <$> getLine
  print $ minimum $ map f xs