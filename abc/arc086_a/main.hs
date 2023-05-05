-- import Data.List
-- main = do
--     [n, k] <- map read . words <$> getLine
--     aList <- words <$> getLine
--     --  ボールの種類ごとの個数をListにする(昇順)
--     let numOfBalls = sort $ map length $ group $ sort aList
--     print $ rewriteCount numOfBalls k 0
-- rewriteCount all@(x:xs) k acc = if length all <= k then acc else rewriteCount xs k (acc + x)
-- rewriteCount [] k acc = 0

import Data.List
main = do
    [n, k] <- map read . words <$> getLine
    aList <- map read . words <$> getLine
    --  ボールの種類ごとの個数をListにする(昇順)
    print $ rewriteCount (sort $ filter (> 0) (numOfBalls aList n)) k 0

numOfBalls xs n = foldl increment (replicate n 0) xs

rewriteCount all@(x:xs) k acc = if length all <= k then acc else rewriteCount xs k (acc + x)
rewriteCount [] k acc = 0

increment xs index = pre ++ [elem + 1] ++ suf
    where pre = take (index - 1) xs
          suf = drop index xs
          elem = xs !! (index - 1)