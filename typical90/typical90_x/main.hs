main = do
  [n, k] <- map read . words <$> getLine
  al <- map read . words <$> getLine
  bl <- map read . words <$> getLine
  -- A: 2つのリストの差分リストを合計する = 2つのリストを同じにするための最低操作回数
  -- B: 入力で与えられた操作回数kからAを引く = 残りの操作回数
  -- Aがkに達していない場合、リストは同一にできないのでNo
  -- Bが偶数の場合はYes, 奇数の場合はNo
  putStrLn $ answer $ (-) k . sum $ diff al bl

-- 2つの数値リストの差分を取ったリストを返す
diff :: [Int] -> [Int] -> [Int]
diff = zipWith (\x y -> abs $ x - y)

answer :: Integral a => a -> String
answer n = if even n && 0 <= n then "Yes" else "No"