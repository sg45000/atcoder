import Control.Monad
main = do
    [n,m] <- map read . words <$> getLine
    ak <- replicateM n getLine
    let sk = map (map read . tail . words) ak
    let ans = foldl (foldl increment) (replicate m 0) sk
    print $ length $ filter (== n) ans



increment xs index = pre ++ [elem + 1] ++ suf
    where pre = take (index - 1) xs
          suf = drop index xs
          elem = xs !! (index - 1)