import Data.List
main = do   
    getLine
    xs <- map read . words <$> getLine
    let a = sum [x | (i, x) <- zip [0..] (reverse $ sort xs), i `mod` 2 == 0]
    let b = sum [x | (i, x) <- zip [0..] (reverse $ sort xs), i `mod` 2 /= 0]
    print (a - b)


-- 別解答
other = do
    getLine
    xs <- map read . words <$> getLine
    print $ sum $ zipWith (*) (cycle [1, -1]) $ reverse $ sort xs