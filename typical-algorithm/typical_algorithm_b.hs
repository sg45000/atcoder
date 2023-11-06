import Control.Monad (replicateM)
import Data.List (sortBy)
import Data.Ord (comparing)

main = do
    n <- readLn
    ab <- replicateM n (map read . words <$> getLine)
    let sortedAB = sortBy (\xy -> compare (x !! 1) (y !! 1)) ab
    sortedAB
