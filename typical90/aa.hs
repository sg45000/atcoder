import Control.Monad
import Data.List
import Data.Map qualified as Map

main = do
    n <- readLn
    ss <- replicateM n getLine
    let lib = solve Map.empty $ zip [1 ..] ss
    mapM_ print $ sort (Map.elems lib)

solve lib [] = lib
solve lib (s : ss) = case Map.lookup (snd s) lib of
    (Just x) -> solve lib ss
    Nothing -> solve lib' ss
      where
        lib' = Map.insert (snd s) (fst s) lib
