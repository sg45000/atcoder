mergeSort [x] = [x]
mergeSort xs = merge (mergeSort $ take i xs) (mergeSort $ drop i xs)
  where
    i = length xs `div` 2
    merge xs [] = xs
    merge [] ys = ys
    merge (x : xs) (y : ys)
        | x <= y = x : merge xs (y : ys)
        | otherwise = y : merge (x : xs) ys
