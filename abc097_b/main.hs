main = do
    x <- readLn
    print $ maximum [sqrt | b <- [1..32], p <- [2..10], let sqrt = b ** p, sqrt <= x]