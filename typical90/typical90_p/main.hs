main = do 
    n <- readLn
    [a,b,c] <- map read . words <$> getLine
    let limit = 9999
    print $ minimum [u + v + w | u <- [0..limit],
     let aSum = u * a,
     v <- [0..(limit- u)],
     let bSum = v * b,
     let cSum = n - aSum - bSum, 
     cSum `mod` c == 0,
     limit - u - v >= 0,
     let w = cSum `div` c
     ]