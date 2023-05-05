import Control.Monad (replicateM)
import Data.Array.ST qualified as Array
import Data.IntMap qualified as IntMap
import Data.Sequence (ViewL (..), ViewR (..), (><))
import Data.Sequence qualified as Seq
import GHC.Arr qualified as Array

bfs :: Int -> IntMap.IntMap Int -> Int -> t
bfs s g n = bfs' (Array.newSTArray (1, n) (-1)) (Seq.fromList [s])
  where
    bfs' visited queue = case Seq.viewl queue of
        EmptyL -> []
        x :< xs -> bfs' newVisited newQueue
      where
        neighbors x = IntMap.findWithDefault [] x g
        newNeighbors

main = do
    n <- readLn
    ab <- replicateM (n - 1) getLine
    let toGraph = map (\[a, b] -> (read a, [read b]))
    let graph = IntMap.fromListWith (++) $ toGraph (map words ab) ++ toGraph (map (reverse . words) ab)
    s