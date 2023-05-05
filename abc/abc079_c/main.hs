main = do
    s <- getLine
    let a = read s !! 0 :: Int
    let b = read s !! 1 :: Int
    let c = read s !! 2 :: Int
    let d = read s !! 3 :: Int
    
    let ans = head [[a, snd u, b, snd v, c, snd w, d] | let operations = [((+), "+"), ((-), "-")], u <- operations, v <- operations, w <- operations, let x = fst u a $ fst v b $  fst w c d, x == 7]
    putStrLn $ concat ans

opeToStr :: p -> String
opeToStr (+) = "+"
opeToStr (-) = "-"
opeToStr x = ""