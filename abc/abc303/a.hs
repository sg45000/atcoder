{-# LANGUAGE TypeApplications #-}

main = do
    _ <- readLn @Int
    s <- getLine
    t <- getLine
    let isSimilar = and $ zipWith similar s t
    let answer = if isSimilar then "Yes" else "No"
    putStrLn answer

similar a b
    | a == b = True
    | a == '0' || a == 'o' = b == '0' || b == 'o'
    | a == '1' || a == 'l' = b == '1' || b == 'l'
    | otherwise = False