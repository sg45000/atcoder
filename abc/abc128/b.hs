import Control.Monad (mapM_, replicateM)
import Data.List (sortBy)

reverseOrdering :: Ordering -> Ordering
reverseOrdering LT = GT
reverseOrdering GT = LT
reverseOrdering _ = EQ

fst' (a, _, _) = a
snd' (_, b, _) = b
trd' (_, _, c) = c

main = do
    n <- readLn
    sps <- replicateM n ((\(a : b : _) -> (a, read b :: Int)) . words <$> getLine)
    let g = zipWith (\(s, p) i -> (s, p, i)) sps [1 ..]
    let spss = sortBy (\a b -> compare (fst' a) (fst' b) `mappend` reverseOrdering (compare (snd' a) (snd' b))) g
    mapM_ (print . trd') spss
