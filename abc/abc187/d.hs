import Control.Monad (replicateM)
import Data.List (find, reverse, sort)
import Data.Maybe (fromJust)
import Data.Ord (compare)

main = do
    n <- readLn
    ab <- replicateM n ((\[a, b] -> (a, b)) . map read . words <$> getLine)
    let effectRanking = reverse . sort $ map calc ab
    let prefixSum = scanl (+) 0 effectRanking
    let voteAllA = sum $ map fst ab
    let answer = fst $ fromJust $ find (\(i, voterToB) -> voterToB > voteAllA) $ zip [0 ..] prefixSum
    print answer

calc (a, b) = 2 * a + b