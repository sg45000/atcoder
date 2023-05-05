import Control.Monad
import Data.List

main = do
  [h, w] <- map read . words <$> getLine
  a <- replicateM h (map read . words <$> getLine) :: IO [[Int]]
  let memoH = [sum line | line <- a]
  let memoW = map sum $ transpose a
  let answer = [ans | (i, h) <- enumerate memoH, (j, w) <- enumerate memoW, let ans = h + w - (a !! i !! j)]
  replicateM h $ print (map (intercalate " ") answer)

enumerate = zip [0 ..]
