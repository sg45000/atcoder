import Data.Bits

main = do
    n <- readLn :: IO Int
    let w =
            [ map (\i -> if i >= 0 then "(" else ")") l
            | b <- [1 .. (2 :: Int) ^ n]
            , let l =
                    [ toRate (b `shiftR` s .&. 1)
                    | s <- reverse [0 .. n - 1]
                    ]
            , check l 0
            ]
    mapM_ (putStrLn . concat) $ reverse w

check :: (Ord t, Num t) => [t] -> t -> Bool
check [] total = total == 0
check (x : xs) total
    | total' >= 0 = check xs total'
    | otherwise = False
  where
    total' = total + x

toRate :: Int -> Int
toRate 0 = -1
toRate 1 = 1