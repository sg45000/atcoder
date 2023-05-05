import Data.Char (chr, ord)
import Data.Map.Strict qualified as Map

main = do
    [n, k] <- map read . words <$> getLine
    s <- getLine
    let a = zip s [1 ..]
    let m = Map.fromListWith (++) $ zipWith (\x y -> (x, [y])) s [1 ..]
    putStrLn $ solve n 0 k m 'a'

solve :: Int -> Int -> Int -> Map.Map Char [Int] -> Char -> String
solve _ _ 0 _ _ = []
solve n i k m c = case Map.lookup c m of
    Nothing -> solve n i k m (chr $ ord c + 1)
    Just is -> case is of
        [] -> solve n i k m (chr $ ord c + 1)
        (x : xs) ->
            if k - 1 <= n - x && i < x
                then c : solve n x (k - 1) (newM xs) c
                else solve n i k (newM xs) c
  where
    newM xs = Map.update (\_ -> Just xs) c m