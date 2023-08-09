import Data.Map qualified as Map

main = do
    [n, k] <- map read . words <$> getLine
    as <- map read . words <$> getLine
    let m = [[] | a <- as]
    teleport m 1 n

isFactorialOfTwo :: Int -> Bool
isFactorialOfTwo n
    | n < 0 = False
    | n <= 2 = True
    | odd n = False
    | otherwise = isFactorialOfTwo (n / 2)

teleport :: Map.Map Int Int -> Int -> Int -> [Int]
teleport m start 0 = []
teleport m start n = next : teleport m next n - 1
  where
    next = m Map.! start
