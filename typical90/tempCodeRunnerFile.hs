import Data.Bits

main = do
    n <- readLn :: IO Int
    let w = [[toRate (b `shiftR` s .&. 1) | s <- [n - 1 .. 0]] | b <- [1 .. (2 :: Int) ^ n]]
    -- let w = [map (\i -> if i >= 0 then "(" else ")") l | b <- [1 .. (2 :: Int) ^ n], let l = [if (b `shiftR` s .&. 1) > 0 then 1 else -1 | s <- [n - 1 .. 0]], check l 0]
    mapM_ print w

check [] total = total == 0
check (x : xs) total
    | total' >= 0 = check xs total'
    | otherwise = False
  where
    total' = total + x

toRate 0 = -1
toRate 1 = 1