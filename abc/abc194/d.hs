{-# LANGUAGE TypeApplications #-}

main = do
    n <- readLn @Integer
    let a = sum [fromIntegral n / fromIntegral i | i <- [1 .. n]]
    print (a - 1) -- 頂点1はすでに訪問済みのため