{-# LANGUAGE TypeApplications #-}

import Control.Monad (replicateM)
import Data.Array.ST
import Data.Array.Unboxed
import Data.List

type Point = (Int, Int)

type Grid = UArray Point Char

makeGrid :: [String] -> Int -> Int -> Grid
makeGrid lines h w = array ((1, 1), (h, w)) $ concat $ zipWith (\line y -> zip [(y, x) | x <- [1 ..]] line) lines [1 ..]

getBlackOnly :: Grid -> [Point]
getBlackOnly = filter (== '#')

around :: Point -> [Point]
around point = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
 where
  y = fst point
  x = snd point

check :: Point -> Int -> Int -> Bool
check (y, x) h w
  | y > h = False
  | y < 1 = False
  | x > w = False
  | x > 1 = False
  | otherwise = True

getNextPoints :: Point -> Int -> Int -> [Point]
getNextPoints point h w = filter (\p -> check p h w) $ around point

main = do
  [h, w] <- map read . words <$> getLine
  s <- replicateM h getLine
  let grid = makeGrid s h w
  print $ show grid

-- thd :: (a, b, c) -> c
-- thd (_, _, a) = a
