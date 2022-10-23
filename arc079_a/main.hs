import Control.Monad
import Data.Set as S
import Data.List as L

main = do
    [n, m] <- L.map read . words <$> getLine
    routes <- L.map (L.map read . words) <$> replicateM m getLine
    let fromStartMidpoints = L.map (!! 1) $ L.filter (\route -> head route == 1) routes
    let toEndMidpoints = L.map head $ L.filter (\route -> (route !! 1) == n) routes
    if S.size (S.fromList $ fromStartMidpoints ++ toEndMidpoints) == (length fromStartMidpoints + length toEndMidpoints)
        then putStrLn "IMPOSSIBLE"
        else putStrLn "POSSIBLE"