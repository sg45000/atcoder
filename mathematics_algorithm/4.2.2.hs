import Data.Array
import Data.List (scanl1)

main = do
    n <- readLn :: IO Int
    t <- readLn :: IO Int
    lr <- map read . words <$> getLine
    let floorDiff = foldl (\acc (l : r : x) -> acc // [(l, acc ! l + 1)] // [(r + 1, acc ! r - 1)]) (listToArray $ replicate t 0) lr
    print $ scanl1 (+) $ elems floorDiff

listToArray :: [a] -> Array Int a
listToArray lst = array (0, length lst - 1) (zip [0 ..] lst)
