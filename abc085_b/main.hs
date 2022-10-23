import Control.Monad ( replicateM )
import Data.List ( group, sort )

main = do
    n <- readLn
    xs <- replicateM n readLn
    print $ length $ group $ sort (xs :: [Integer])
