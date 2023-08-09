import Control.Monad (replicateM)
import Data.Array

bfs start visited maze h w = bfs'
  where
    neighbors [y, x] = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    inRange h w [y, x] = 0 <= y && y < h && 0 <= x && x < w
    isWall m [y, x] = (m ! y ! x) == '#'
    canProceed m h w cell = inRange h w cell && not isWall m cell
    next = filter canProceed neighbors
    newVisited = map

main = do
    [h, w] <- map read . words <$> getLine
    ss <- replicateM h getLine
    let ssArr = array (0, length ss - 1) (zip [0 ..] ss)
