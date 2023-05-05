{-# LANGUAGE TypeApplications #-}

main = do
    n <- readLn
    distances <- map read . words <$> getLine
    via <- map read . words <$> getLine
    print $ [v | v <- [0 .. length via - 1]]

finiteDifference :: Num a => [a] -> [a] -> [a]
finiteDifference = foldl (\fd x1 -> fd ++ [last fd + x1])

resolve :: Num a => [a] -> [a] -> a -> a -> a
resolve [] fd s g = 0
resolve (v : vs) fd s g = fd !! (g - 1) - fd !! (s - 1) + resolve vs fd g v