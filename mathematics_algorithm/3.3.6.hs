import Data.Array (Array, listArray, (!), (//))

main = do
    cards <- map read . words <$> getLine
    let a = foldl up ini cards
    print $ sum [(a ! b) `xcy` (a ! c) | b <- [1 .. 49999], let c = 100000 - b]

ini :: Array Integer Integer
ini = listArray (1, 99999) (replicate 99999 0)

up arr n = arr // [(n, (arr ! n) + 1)]
xcy x y = factorial' x `div` factorial' (x - y)
factorial' 1 = 1
factorial' x = x * factorial' (x - 1)
